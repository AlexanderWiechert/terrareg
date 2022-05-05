
integration_git_providers = {
    1: {
        'name': 'testgitprovider',
        'base_url_template': 'https://localhost.com/{namespace}/{module}-{provider}',
        'browse_url_template': 'https://localhost.com/{namespace}/{module}-{provider}/browse/{tag}/{path}',
        'clone_url_template': 'ssh://localhost.com/{namespace}/{module}-{provider}'
    },
    2: {
        'name': 'repo_url_tests',
        'base_url_template': 'https://base-url.com/{namespace}/{module}-{provider}',
        'browse_url_template': 'https://browse-url.com/{namespace}/{module}-{provider}/browse/{tag}/{path}suffix',
        'clone_url_template': 'ssh://clone-url.com/{namespace}/{module}-{provider}'
    }
}

integration_test_data = {
    'testnamespace': {
        'wrongversionorder': {'testprovider': {
            'id': 17,
            'versions': {
                '1.5.4': {'published': True}, '2.1.0': {'published': True}, '0.1.1': {'published': True},
                '10.23.0': {'published': True}, '0.1.10': {'published': True}, '0.0.9': {'published': True},
                '0.1.09': {'published': True}, '0.1.8': {'published': True}
            }
        }}
    },
    'moduleextraction': {
        'test-module': { 'testprovider': {
            'id': 7,
            'repo_clone_url_template': 'ssh://example.com/repo.git'
        }},
        'bitbucketexample': {
            'testprovider': {
                'id': 8,
                'repo_clone_url_template': 'ssh://git@localhost:7999/bla/test-module.git',
                'git_tag_format': 'v{version}',
                'versions': []
            }
        },
        'gitextraction': {
            'staticrepourl': {
                'id': 9,
                'repo_clone_url_template': 'ssh://git@localhost:7999/bla/test-module.git',
                'git_tag_format': 'v{version}',
                'versions': []
            },
            'placeholdercloneurl': {
                'id': 10,
                'repo_clone_url_template': 'ssh://git@localhost:7999/{namespace}/{module}-{provider}.git',
                'git_tag_format': 'v{version}',
                'versions': []
            },
            'usesgitprovider': {
                'id': 11,
                'git_provider_id': 1,
                'git_tag_format': 'v{version}',
                'versions': []
            },
            'nogittagformat': {
                'id': 12,
                'git_provider_id': 1,
                'versions': []
            },
            'complexgittagformat': {
                'id': 13,
                'git_provider_id': 1,
                'git_tag_format': 'unittest{version}value',
                'versions': []
            },
            'norepourl': {
                'id': 14,
                'git_tag_format': 'v{version}',
                'versions': []
            }
        },
    },
    'real_providers': {
        'test-module': {
            'aws': {
                'id': 22,
                'versions': {
                    '1.0.0': {}
                }
            },
            'gcp': {
                'id': 23,
                'versions': {
                    '1.0.0': {}
                }
            },
            'doesnotexist': {
                'id': 24,
                'versions': {
                    '1.0.0': {}
                }
            }
        }
    },
    'repo_url_tests': {
        'no-git-provider': {'test': {
            'id': 18,
            'versions': {
                '1.0.0': {},
                '1.4.0': {
                    'repo_base_url_template': 'https://mv-base-url.com/{namespace}/{module}-{provider}',
                    'repo_browse_url_template': 'https://mv-browse-url.com/{namespace}/{module}-{provider}/browse/{tag}/{path}suffix',
                    'repo_clone_url_template': 'ssh://mv-clone-url.com/{namespace}/{module}-{provider}'
                }
            }
        }},
        'git-provider-urls': {'test': {
            'id': 19,
            'versions': {
                '1.1.0': {},
                '1.4.0': {
                    'repo_base_url_template': 'https://mv-base-url.com/{namespace}/{module}-{provider}',
                    'repo_browse_url_template': 'https://mv-browse-url.com/{namespace}/{module}-{provider}/browse/{tag}/{path}suffix',
                    'repo_clone_url_template': 'ssh://mv-clone-url.com/{namespace}/{module}-{provider}'
                }
            },
            'git_provider_id': 2
        }},
        'module-provider-urls': { 'test': {
            'id': 20,
            'versions': {
                '1.2.0': {},
                '1.4.0': {
                    'repo_base_url_template': 'https://mv-base-url.com/{namespace}/{module}-{provider}',
                    'repo_browse_url_template': 'https://mv-browse-url.com/{namespace}/{module}-{provider}/browse/{tag}/{path}suffix',
                    'repo_clone_url_template': 'ssh://mv-clone-url.com/{namespace}/{module}-{provider}'
                }
            },
            'repo_base_url_template': 'https://mp-base-url.com/{namespace}/{module}-{provider}',
            'repo_browse_url_template': 'https://mp-browse-url.com/{namespace}/{module}-{provider}/browse/{tag}/{path}suffix',
            'repo_clone_url_template': 'ssh://mp-clone-url.com/{namespace}/{module}-{provider}'
        }},
        'module-provider-override-git-provider': { 'test': {
            'id': 21,
            'versions': {
                '1.3.0': {},
                '1.4.0': {
                    'repo_base_url_template': 'https://mv-base-url.com/{namespace}/{module}-{provider}',
                    'repo_browse_url_template': 'https://mv-browse-url.com/{namespace}/{module}-{provider}/browse/{tag}/{path}suffix',
                    'repo_clone_url_template': 'ssh://mv-clone-url.com/{namespace}/{module}-{provider}'
                }
            },
            'repo_base_url_template': 'https://mp-base-url.com/{namespace}/{module}-{provider}',
            'repo_browse_url_template': 'https://mp-browse-url.com/{namespace}/{module}-{provider}/browse/{tag}/{path}suffix',
            'repo_clone_url_template': 'ssh://mp-clone-url.com/{namespace}/{module}-{provider}',
            'git_provider_id': 2
        }}
    },
    'modulesearch': {
        'contributedmodule-oneversion': {'aws': {
            'id': 25,
            'versions': {'1.0.0': {'published': True}}
        }},
        'contributedmodule-multiversion': {'aws': {
            'id': 26,
            'versions': {
                '1.2.3': {'published': True},
                '2.0.0': {'published': True}
            }
        }},
        'contributedmodule-differentprovider': {'gcp': {
            'id': 27,
            'versions': {
                '1.2.3': {'published': True}
            }
        }},
        'contributedmodule-unpublished': {'aws': {
            'id': 28,
            'versions': {
                '1.0.0': {}
            }
        }},
        'verifiedmodule-oneversion': {'aws': {
            'verified': True,
            'id': 29,
            'versions': {'1.0.0': {'published': True}}
        }},
        'verifiedmodule-multiversion': {'aws': {
            'verified': True,
            'id': 30,
            'versions': {
                '1.2.3': {'published': True},
                '2.0.0': {'published': True}
            }
        }},
        'verifiedmodule-differentprovider': {'gcp': {
            'verified': True,
            'id': 31,
            'versions': {
                '1.2.3': {'published': True}
            }
        }},
        'verifiedmodule-unpublished': {'aws': {
            'verified': True,
            'id': 32,
            'versions': {
                '1.0.0': {}
            }
        }}
    },
    'modulesearch-contributed': {
        'mixedsearch-result': {'aws': {
            'id': 33,
            'versions': {'1.0.0': {'published': True}}
        }},
        'mixedsearch-result-multiversion': {'aws': {
            'id': 34,
            'versions': {
                '1.2.3': {'published': True},
                '2.0.0': {'published': True}
            }
        }},
        'mixedsearch-result-unpublished': {'aws': {
            'id': 35,
            'versions': {
                '1.2.3': {},
                '2.0.0': {}
            }
        }},
    },
    'modulesearch-trusted': {
        'mixedsearch-trusted-result': {'aws': {
            'id': 36,
            'versions': {'1.0.0': {'published': True}}
        }},
        'mixedsearch-trusted-second-result': {'aws': {
            'id': 37,
            'versions': {
                '5.2.1': {'published': True},
            }
        }},
        'mixedsearch-trusted-result-multiversion': {'aws': {
            'id': 38,
            'versions': {
                '1.2.3': {'published': True},
                '2.0.0': {'published': True}
            }
        }},
        'mixedsearch-trusted-result-unpublished': {'aws': {
            'id': 39,
            'versions': {
                '1.2.3': {},
                '2.0.0': {}
            }
        }},
    },
    'searchbynamespace': {
        'searchbymodulename1': {
            'searchbyprovideraws': {
                'id': 40,
                'versions': {
                    '1.2.3': {'published': True}
                }
            },
            'searchbyprovidergcp': {
                'id': 41,
                'versions': {
                    '2.0.0': {'published': True}
                }
            }
        },
        'searchbymodulename2': {
            'notpublished': {
                'id': 42,
                'versions': {'1.2.3': {}}
            },
            'published': {
                'id': 43,
                'versions': {
                    '3.1.6': {'published': True}
                }
            }
        }
    },
    'searchbynamesp-similar': {
        'searchbymodulename3': {'searchbyprovideraws': {
            'id': 44,
            'versions': {'4.4.1': {'published': True}}
        }},
        'searchbymodulename4': {'aws': {
            'id': 45,
            'versions': {'5.5.5': {'published': True}}
        }}
    }
}