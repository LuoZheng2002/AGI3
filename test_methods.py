from Kernel.Struct.bytecode_format import r
from Kernel.Struct.system_functions import sc
from test_method_codes import mc
test_method = [
    [r['if'], [r['system_call'], sc['=='], [[101], [100]]],
        [
           [r['return'], [r['concept_instance'], 100]]
        ],
        [
            [[r['system_call'], sc['=='], [[1], [2]]], [[r['return'], [r['concept_instance'], 101]]]],
            [[r['system_call'], sc['>'], [[2], [2]]], [[r['return'], [r['concept_instance'], 102]]]],
            [[r['system_call'], sc['<='], [[1], [0]]], [[r['return'], [r['concept_instance'], 103]]]],
        ],
        [
            [r['return'], [r['concept_instance'], 104]]
        ]
    ]
]


vertical_add = [
    [r['assign'], [r['reg'], 0, []], [r['concept_instance'], 2]],
    [r['for'], 0,
        # end value
        [r['system_call'], sc['max'],
            [
                [r['size'], [r['input'], 0]],
                [r['size'], [r['input'], 1]]
            ]
        ],
        # for lines
        [
            [r['if'],
                # if statement for judging
                [r['system_call'], sc['and'],
                    [
                        [r['system_call'], sc['<'],
                            [
                                [r['iterator'], 0],
                                [r['size'], [r['input'], 0]]
                            ]
                        ],
                        [r['system_call'], sc['<'],
                            [
                                [r['iterator'], 0],
                                [r['size'], [r['input'], 1]]
                             ]
                        ]
                    ]
                ],
                # if lines
                [
                    # a single line in the block
                    [r['assign'],
                        [r['reg'], 1, [[r['iterator'], 0]]],
                        [r['call'], mc['digit sum'],
                            [
                                [r['call'], mc['digit to number'],
                                    [
                                        [r['at_reverse'], [r['input'], 0], [r['iterator'], 0]]
                                    ]
                                ],
                                [r['call'], mc['digit to number'],
                                    [
                                        [r['at_reverse'], [r['input'], 1], [r['iterator'], 0]]
                                    ]
                                ]
                            ]
                        ]
                    ]
                ],
                # else if blocks
                [
                    # else if block 1
                    [
                        # else if statement 1 for judging
                        [r['system_call'], sc['and'],
                            [
                                [r['system_call'], sc['<'],
                                    [
                                        [r['iterator'], 0],
                                        [r['size'], [r['input'], 0]]
                                    ]
                                ],
                                [r['system_call'], sc['>='],
                                    [
                                        [r['iterator'], 0],
                                        [r['size'], [r['input'], 1]]
                                    ]
                                ]
                            ]
                        ],
                        # else if 1 lines
                        [
                            [r['assign'],
                                [r['reg'], 1, [[r['iterator'], 0]]],
                                [r['call'], mc['digit to number'],
                                    [
                                        [r['at_reverse'],
                                            [r['input'], 0],
                                            [r['iterator'], 0]
                                        ]
                                    ]
                                ]
                            ]
                        ]
                    ],
                    # else if block 2
                    [
                        # else if statement 2 for judging
                        [r['system_call'], sc['and'],
                            [
                                [r['system_call'], sc['>='],
                                    [
                                        [r['iterator'], 0],
                                        [r['size'], [r['input'], 0]]
                                    ]
                                ],
                                [r['system_call'], sc['<'],
                                    [
                                        [r['iterator'], 0],
                                        [r['size'], [r['input'], 1]]
                                     ]
                                ]
                            ]
                        ],
                        # else if 2 lines
                        [
                            [r['assign'],
                                [r['reg'], 1, [[r['iterator'], 0]]],
                                [r['call'], mc['digit to number'],
                                    [
                                        [r['at_reverse'],
                                            [r['input'], 1],
                                            [r['iterator'], 0]
                                        ]
                                    ]
                                ]
                            ]
                        ]
                    ]
                ],
                # else lines
                []
            ],
            [r['if'],
                # if statement for judging
                [r['system_call'], sc['and'],
                    [
                        [r['system_call'], sc['>='],
                            [
                                [r['iterator'], 0],
                                [1]
                            ]
                        ],
                        [r['system_call'], sc['=='],
                            [
                                [r['size'],
                                    [r['reg'], 3,
                                        [
                                            [r['system_call'], sc['offset'],
                                                [
                                                    [r['iterator'], 0],
                                                    [-1]
                                                ]
                                            ]
                                        ]
                                    ]
                                ],
                                [2]
                            ]
                        ]
                    ]
                ],
                # if lines
                [
                    [r['assign'],
                        [r['reg'], 2, [[r['iterator'], 0]]],
                        [r['call'], mc['digit sum'],
                            [
                                [r['call'], mc['digit to number'],
                                    [
                                        [r['at_reverse'],
                                            [r['reg'], 1, [[r['iterator'], 0]]],
                                            [0]
                                        ]
                                    ]
                                ],
                                [r['call'], mc['digit to number'],
                                    [
                                        [r['at_reverse'],
                                            [r['reg'], 3,
                                                [
                                                    [r['system_call'], sc['offset'],
                                                        [
                                                            [r['iterator'], 0],
                                                            [-1]
                                                        ]
                                                    ]
                                                ]
                                            ],
                                            [1]
                                        ]
                                    ]
                                ]
                            ]
                        ]
                    ],
                    [r['if'],
                        # if statement for judging
                        [r['system_call'], sc['=='],
                            [
                                [r['size'], [r['reg'], 1, [[r['iterator'], 0]]]],
                                [2]
                            ]
                        ],
                        # if lines
                        [
                            [r['assign'], [r['reg'], 3, [[r['iterator'], 0]]], [r['concept_instance'], 2]],
                            [r['assign'],
                                [r['at_reverse'],
                                    [r['reg'], 3, [[r['iterator'], 0]]],
                                    [0]
                                ],
                                [r['at_reverse'],
                                    [r['reg'], 2, [[r['iterator'], 0]]],
                                    [0]
                                ]
                            ],
                            [r['assign'],
                                [r['at_reverse'],
                                    [r['reg'], 3, [[r['iterator'], 0]]],
                                    [1]
                                ],
                                [r['at_reverse'],
                                    [r['reg'], 1, [[r['iterator'], 0]]],
                                    [1]
                                ]
                            ]
                        ],
                        # else if blocks
                        [],
                        # else lines
                        [
                            [r['assign'],
                                [r['reg'], 3, [[r['iterator'], 0]]],
                                [r['reg'], 2, [[r['iterator'], 0]]]
                            ]
                        ]
                    ]
                ],
                # else if blocks
                [],
                # else lines
                [
                    [r['assign'],
                        [r['reg'], 3, [[r['iterator'], 0]]],
                        [r['reg'], 1, [[r['iterator'], 0]]]
                    ]
                ]
            ],
            [r['assign'],
                [r['at_reverse'],
                    [r['reg'], 0, []],
                    [r['iterator'], 0]
                ],
                [r['at_reverse'],
                    [r['reg'], 3, [[r['iterator'], 0]]],
                    [0]
                ]
            ]
        ]
    ],
    [r['if'],
        # if statement for judging
        [r['system_call'], sc['=='],
            [
                [r['size'],
                    [r['reg'], 3,
                        [
                            [r['system_call'], sc['offset'],
                                [
                                    [r['system_call'], sc['max'],
                                        [
                                            [r['size'], [r['input'], 0]],
                                            [r['size'], [r['input'], 1]]
                                        ]
                                    ],
                                    [-1]
                                ]
                            ]
                        ]
                    ]
                ],
                [2]
            ]
        ],
        # if lines
        [
            [r['assign'],
                [r['at_reverse'],
                    [r['reg'], 0, []],
                    [r['system_call'], sc['max'],
                        [
                            [r['size'], [r['input'], 0]],
                            [r['size'], [r['input'], 1]]
                        ]
                    ]
                ],
                [r['at_reverse'],
                    [r['reg'], 3,
                        [
                            [r['system_call'], sc['offset'],
                                [
                                    [r['system_call'], sc['max'],
                                        [
                                            [r['size'], [r['input'], 0]],
                                            [r['size'], [r['input'], 1]]
                                        ]
                                    ],
                                    [-1]
                                ]
                            ]
                        ]
                    ],
                    [1]
                ]
            ]
        ],
        # else if blocks
        [],
        # else lines
        []
    ],
    [r['return'], [r['reg'], 0, []]]
]