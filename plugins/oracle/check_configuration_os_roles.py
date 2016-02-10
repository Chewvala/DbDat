class check_configuration_os_roles():
    """
    check_configuration_os_roles:
    The	os_roles setting permits externally	created	groups to be applied to	database
    management.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

    TITLE    = 'OS Roles'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='OS_ROLES'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if 'TRUE' == row[0]:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'OS Roles is (%s) enabled.' % (row[0])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'OS Roles is (%s) not enabled.' % (row[0])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
