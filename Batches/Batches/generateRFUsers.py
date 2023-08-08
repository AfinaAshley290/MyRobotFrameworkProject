groups={'citi.com':['citi','A'],
        'rbos.com':['rbos','B'],
        'soge.com':['soge','C'],
        'sarb.com':['sarb','D'],
        'sola.com':['sola','S'],
        'agri.com':['agri','R'],
        'bnpparibas.com':['parb','P'],
        'arba.com':['arba','I'],
        'bkch.com':['bkch','4J'],
        'hsbc.com':['hsbc','4H'],
        'swift.com':['swift','SW'],
        'cajarural.com':['cajarural','RA'],
        'cpm.co.ma':['cpm','RB'],
        'bes.pt':['bes','RC'],
        'abchina.com':['abchina','RD'],
        }
roles=['submitter',
       'approver',
       'requester',
       'granter',
       'administrator',
       'viewer',
       'swprequester',
       'swpgranter',
       'swppublisher',
       'swpviewer']
swiftRoles=['submitter',
            'approver',
            'qualifier',
            'publisher',
            'administrator']
for domain,group in groups.items():
    if group[1] =='SW':
        for role in swiftRoles:
            for i in range(1,3):
                print "${%s_%s%d_user}    pac.kyc.%s%d@%s" % (role,group[1],i,role,i,domain)
                print "${%s_%s%d_name}    %s %s%d" % (role,group[1],i,group[0],role,i)
    else:
        for role in roles:
            for i in range(1,3):
                print "${%s_%s%d_user}    pac.kyc.%s%d@%s" % (role,group[1],i,role,i,domain)
                print "${%s_%s%d_name}    %s %s%d" % (role,group[1],i,group[0],role,i)

