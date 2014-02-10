{
    'variables': {
    },

    'targets': [
        {
            'target_name': 'office-space',
            'type': 'shared_library',

            #'dependencies': [
            #    'node_js2c#host',
            #],

            'include_dirs': [
                'src',
            ],

            'sources': [
                'src/driver.c'
            ],

            'defines': [
                'OS_DRIVER_VERSION="0.0.1"',
            ],
        },
    ] # end targets
}
