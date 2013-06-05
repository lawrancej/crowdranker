# -*- coding: utf-8 -*-

from gluon import current

# Parameters for job queues.
REPUTATION_SYSTEM_QUEUE = 'repsys-queue'
REPUTATION_SYSTEM_RUN_URL = '/crowdgrader/queues/run_rep_sys/'
REPUTATION_SYSTEM_PARAM_NUM_ITERATIONS = 'n_iterations'
REPUTATION_SYSTEM_PARAM_VENUE_ID = 'venue_id'
REPUTATION_SYSTEM_PARAM_REVIEW_PERCENTAGE = 'review_percentage'
REPUTATION_SYSTEM_STARTOVER = 'startover'
REPUTATION_SYSTEM_ALGO = 'algo'
REPUTATION_SYSTEM_RUN_ID = 'run_id'
REPUTATION_SYSTEM_PUBLISH = 'publish'
# Below are the options for convex optimization.
REPUTATION_SYSTEM_COST_TYPE = 'cost_type'
REPUTATION_SYSTEM_POS_SLOPE = 'pos_slope'
REPUTATION_SYSTEM_NEG_SLOPE = 'neg_slope'
REPUTATION_SYSTEM_NORMALIZE_GRADES = 'normalize_grades'
REPUTATION_SYSTEM_NORMALIZATION_SCALE = 'normalization_scale'
REPUTATION_SYSTEM_NORMALIZE_EACH_ITER = 'normalize_each_iteration'
REPUTATION_SYSTEM_USE_SUBMISSION_RANK_IN_REP = 'use_rank_in_rep'
REPUTATION_SYSTEM_SUBMISSION_RANK_REP_EXP = 'rank_rep_exp'
REPUTATION_SYSTEM_REPUTATION_METHOD = 'reputation_method'
REPUTATION_SYSTEM_PREC_COEFF = 'prec_coeff'
REPUTATION_SYSTEM_PREC_METHOD = 'prec_method'
# Below are the options for Vancouver.
REPUTATION_SYSTEM_DO_DEBIAS = 'do_debias'
REPUTATION_SYSTEM_USE_MEDIAN = 'use_median'
REPUTATION_SYSTEM_USE_REPUTATION = 'use_reputation'

# Makes the above available to modules.
current.REPUTATION_SYSTEM_QUEUE = REPUTATION_SYSTEM_QUEUE
current.REPUTATION_SYSTEM_RUN_URL = REPUTATION_SYSTEM_RUN_URL
current.REPUTATION_SYSTEM_PARAM_NUM_ITERATIONS = REPUTATION_SYSTEM_PARAM_NUM_ITERATIONS
current.REPUTATION_SYSTEM_PARAM_VENUE_ID = REPUTATION_SYSTEM_PARAM_VENUE_ID
current.REPUTATION_SYSTEM_PARAM_REVIEW_PERCENTAGE = REPUTATION_SYSTEM_PARAM_REVIEW_PERCENTAGE
current.REPUTATION_SYSTEM_STARTOVER = REPUTATION_SYSTEM_STARTOVER
current.REPUTATION_SYSTEM_ALGO = REPUTATION_SYSTEM_ALGO
current.REPUTATION_SYSTEM_RUN_ID = REPUTATION_SYSTEM_RUN_ID
current.REPUTATION_SYSTEM_PUBLISH = REPUTATION_SYSTEM_PUBLISH
current.REPUTATION_SYSTEM_COST_TYPE = REPUTATION_SYSTEM_COST_TYPE
current.REPUTATION_SYSTEM_POS_SLOPE = REPUTATION_SYSTEM_POS_SLOPE
current.REPUTATION_SYSTEM_NEG_SLOPE = REPUTATION_SYSTEM_NEG_SLOPE
current.REPUTATION_SYSTEM_NORMALIZE_GRADES = REPUTATION_SYSTEM_NORMALIZE_GRADES
current.REPUTATION_SYSTEM_NORMALIZATION_SCALE = REPUTATION_SYSTEM_NORMALIZATION_SCALE
current.REPUTATION_SYSTEM_NORMALIZE_EACH_ITER = REPUTATION_SYSTEM_NORMALIZE_EACH_ITER
current.REPUTATION_SYSTEM_USE_SUBMISSION_RANK_IN_REP = REPUTATION_SYSTEM_USE_SUBMISSION_RANK_IN_REP
current.REPUTATION_SYSTEM_SUBMISSION_RANK_REP_EXP = REPUTATION_SYSTEM_SUBMISSION_RANK_REP_EXP
current.REPUTATION_SYSTEM_REPUTATION_METHOD = REPUTATION_SYSTEM_REPUTATION_METHOD
current.REPUTATION_SYSTEM_PREC_COEFF = REPUTATION_SYSTEM_PREC_COEFF
current.REPUTATION_SYSTEM_PREC_METHOD = REPUTATION_SYSTEM_PREC_METHOD
current.REPUTATION_SYSTEM_DO_DEBIAS = REPUTATION_SYSTEM_DO_DEBIAS
current.REPUTATION_SYSTEM_USE_MEDIAN = REPUTATION_SYSTEM_USE_MEDIAN
current.REPUTATION_SYSTEM_USE_REPUTATION = REPUTATION_SYSTEM_USE_REPUTATION

# Algorithm names
ALGO_OPT = 'opt'
ALGO_DISTR = 'distr'
ALGO_VANCOUVER = 'vancouver'
ALGO_DISTR_NOREP = 'distr'
ALGO_LIST = [ALGO_OPT, ALGO_DISTR, ALGO_VANCOUVER]
ALGO_DEFAULT = ALGO_VANCOUVER
ALGO_PREC_METHOD_DIST = 'stdev'
ALGO_PREC_METHOD_CORR = 'corr'
current.ALGO_PREC_METHOD_DIST = ALGO_PREC_METHOD_DIST
current.ALGO_PREC_METHOD_CORR = ALGO_PREC_METHOD_CORR
# Type of matrix D
REPUTATION_SYSTEM_MATRIX_D_TYPE = "matrix_D_type"
MATRIX_D_TYPE_GRADES_DIST = "distance_between_grades"
MATRIX_D_TYPE_GRADES_SINGLE = "single_grades"
current.MATRIX_D_TYPE_GRADES_DIST = MATRIX_D_TYPE_GRADES_DIST
current.MATRIX_D_TYPE_GRADES_SINGLE = MATRIX_D_TYPE_GRADES_SINGLE

# Algo defaults
ALGO_DEFAULT_COST_TYPE = 'linear'
ALGO_DEFAULT_POS_SLOPE = 1.0
ALGO_DEFAULT_NEG_SLOPE = 4.0
ALGO_DEFAULT_NUM_ITERATIONS = 10
ALGO_DEFAULT_NORMALIZE = True
ALGO_DEFAULT_NORMALIZATION_SCALE = 1.0
ALGO_DEFAULT_REVIEWS_AS_PERCENTAGE = 25.0
current.ALGO_DEFAULT_REVIEWS_AS_PERCENTAGE = ALGO_DEFAULT_REVIEWS_AS_PERCENTAGE
ALGO_DEFAULT_USE_RANK_IN_REPUTATION = True
ALGO_DEFAULT_RANK_REP_EXP = 0.7
ALGO_DEFAULT_PREC_COEFF = 1.0
ALGO_DEFAULT_REPUTATION_METHOD = 'cost'
ALGO_DEFAULT_PREC_METHOD = 'stdev'
# Vancouver.
ALGO_DEFAULT_DO_DEBIAS = False
ALGO_DEFAULT_USE_MEDIAN = False
ALGO_DEFAULT_USE_REPUTATION = True