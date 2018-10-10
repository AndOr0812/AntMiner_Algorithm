from terms import *


def ant_miner(dataset, no_of_ants, min_case_per_rule, max_uncovered_cases, no_rules_converg):

    TrainingSet = dataset.data
    list_of_terms = get_terms(dataset)
    DiscoveredRuleList = []

    while TrainingSet > max_uncovered_cases:

        ant_index = 0
        converg_test_index = 0

        PheromoneInit()
        HeuristicCalculation()

        while True:

            ant_index += 1

            RuleConstruction()
            RulePrune()
            PheromoneUpdating()

            CheckConverg()

            if ant_index >= no_of_ants or converg_test_index >= no_rules_converg:
                break

        R_best = ChoosesBestRule()
        DiscoveredRuleList.append(R_best)
        covered_cases = get_CoveredCases
        TrainingSet = TrainingSet - covered_cases

    return DiscoveredRuleList