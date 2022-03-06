from attr import validate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from portfolio.models import Currency, Portfolio
from tax_analysis.db.processing_analysis import create_analysis
from tax_analysis.models import PortfolioAnalysis, AnalysisAlgorithm, MiningTaxMethod, PortfolioAnalysisReport


class PortfolioReportCreateSerializer(serializers.ModelSerializer):

    # base_currency = serializers.RelatedField(queryset=Currency.objects.all(), read_only=True)
    algo = serializers.ChoiceField(choices=AnalysisAlgorithm.choices, default=AnalysisAlgorithm.ALGO_FIFO)
    transfer_algo = serializers.ChoiceField(choices=AnalysisAlgorithm.choices, default=AnalysisAlgorithm.ALGO_FIFO)
    untaxed_allowance = serializers.FloatField(min_value=0)
    mining_tax_method = serializers.ChoiceField(choices=MiningTaxMethod.choices,
                                                default=MiningTaxMethod.ON_DEPOSIT_AND_GAINS)
    mining_deposit_profit_rate = serializers.FloatField(min_value=0.0, max_value=1.0, allow_null=False)
    cross_wallet_sells = serializers.BooleanField()
    taxable_period_days = serializers.IntegerField(min_value=1, max_value=1000000, allow_null=True)

    class Meta:
        model = PortfolioAnalysis
        fields = (
            'base_currency',
            'algo', 'transfer_algo',
            'untaxed_allowance',
            'mining_tax_method', 'mining_deposit_profit_rate',
            'cross_wallet_sells', 'taxable_period_days'
        )

    def __init__(self, uid, pid, *args, **kwargs):
        self.uid = uid
        self.pid = pid
        super().__init__(*args, **kwargs)

    def clean_portfolio(self):
        pf = Portfolio.objects.filter(id=self.pid)
        if not pf.exists():
            raise ValidationError("portfolio does not exist")
        # access control
        if pf.first().user_id != self.uid:
            raise ValidationError("insufficient rights")

        return pf.first()

    def validate(self, attrs):
        self.portfolio = self.clean_portfolio()
        return attrs

    def create(self, validated_data):
        # settings
        base_currency = validated_data['base_currency']
        algo = validated_data['algo']
        transfer_algo = validated_data['transfer_algo']
        untaxed_allowance = validated_data['untaxed_allowance']
        mining_tax_method = validated_data['mining_tax_method']
        mining_deposit_profit_rate = validated_data['mining_deposit_profit_rate']
        cross_wallet_sells = validated_data['cross_wallet_sells']
        taxable_period_days = validated_data['taxable_period_days']

        analysis_id = create_analysis(
            self.portfolio.id, base_currency,
            algo, transfer_algo,
            untaxed_allowance,
            mining_tax_method, mining_deposit_profit_rate,
            cross_wallet_sells, taxable_period_days
        )

        return analysis_id
