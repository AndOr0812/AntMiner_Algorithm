from functions import *


def ant_miner(dataset, no_of_ants, min_case_per_rule, max_uncovered_cases, no_rules_converg):

    TrainingSet = dataset
    DiscoveredRuleList = []

    while len(TrainingSet.data) > max_uncovered_cases:

        list_of_terms = get_terms(TrainingSet.attr_values)
        ant_index = 0
        converg_test_index = 0

        set_pheromone_init(list_of_terms)

        set_heuristic_values(list_of_terms, TrainingSet)

        while True:

            ant_index += 1

            current_rule_list = []
            current_rule = cRule(TrainingSet)

            rule_construction(current_rule, list_of_terms, min_case_per_rule, TrainingSet)

            current_rule.set_quality(TrainingSet)

            rule_pruning(current_rule, min_case_per_rule, TrainingSet)

            current_rule_list.append(current_rule)

            # PheromoneUpdating()

            # CheckConverg()

            if ant_index >= no_of_ants:
                break
            elif converg_test_index >= no_rules_converg:
                break

        # R_best = ChoosesBestRule()
        # DiscoveredRuleList.append(R_best)
        # covered_cases = get_CoveredCases
        # TrainingSet = TrainingSet - covered_cases

    return DiscoveredRuleList



