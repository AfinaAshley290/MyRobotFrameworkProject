import os, re,ldap
from pprint import pprint

class SdCIDMUser():
    """
    It's an IDM user with all it's profiles. Generaly populated from ldap call.
    """
    def __init__(self,email,password=""):
        self.email=email
        self.password=password
        self.firstName=""
        self.lastName=""
        self.swift2faIsMandatory=""
        self.swift2faActivated=""
        self.loadedFromLdap=False
        self.profileIds={}
    def isMultiprofile(self):
        if len(self.profileIds)>1:
            return True
        else:
            return False
    def getProfileIdForBIC(self,bic=""):
        if bic and bic in self.profileIds.keys():
            return [bic,self.profileIds[bic]]
        elif self.profileIds:
            return [self.profileIds.items()[0][0],self.profileIds.items()[0][1]]
        else:
            return []
    def setProfileId(self,bic,profileId):
        self.profileIds[bic]=profileId
    def getSdCUser(self,bic=""):
        user = SdCUser(self.email,bic,self.password)
        user.firstName = self.firstName
        user.lastName=self.lastName
        profId=self.getProfileIdForBIC(bic)
        if profId:
            user.bic=profId[0]
            user.profileId=profId[1]
        if self.isMultiprofile():
            user.isMultiprofile=True
        return user
    def __str__(self):
        return dump(self)
def loadUserProfileFromLdap(RFUsers):
    """
    Return a list of SdCIDMUser(s) from LDAP
    """
    sdCIDMUsers={}
    try:
        print "Connecting to ldap"
        print "Server: %s" % server
        print "Port: %s" % port
        print "User: %s" % ldapUser
        l = ldap.open(server, port=port)
        l.protocol_version = ldap.VERSION3
        username = ldapUser
        password = ldapPassword
        l.simple_bind(username, password)
        print "Connected"
    except ldap.LDAPError, e:
        print e
        return False
    baseDN = ldapBaseDN
    searchScope = ldap.SCOPE_SUBTREE
    retrieveAttributes = None
    for usr in RFUsers.values():
        email=usr['email']
        print "Searching ldap for user %s" % (email)
        user=SdCIDMUser(email)
        try:
            user.firstName = usr['firstname']
            user.lastName = usr['lastname']
        except:
            print 'User without names !!!!', usr

        searchFilter = "mail="+email+"*"
        ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        while 1:
            result_type, result_data = l.result(ldap_result_id, 0)
            if not result_data:
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    email = result_data[0][1]['mail'][0]
                    try:
                        res=result_data[0][1]
                        SwiftProfileId = res['swiftProfileId'][0]
                        bic = res['swiftBicId'][0]
                        user.firstName = res['givenName'][0]
                        user.lastName = res['sn'][0]
                        user.setProfileId(bic, SwiftProfileId)
                        if 'swift2faIsMandatory' in res.keys():
                            user.swift2faIsMandatory = res['swift2faIsMandatory'][0]
                        if 'swift2faActivated' in res.keys():
                            user.swift2faActivated = res['swift2faActivated'][0]
                        user.loadedFromLdap=True
                        print "Found user: %s, %s, %s" % (email, bic, SwiftProfileId)
                    except:
                        pass
        sdCIDMUsers[email]=user
    return sdCIDMUsers

# MAIN

server = 'bedset20'
port=20391
ldapUser='cn=Directory Manager'
ldapPassword='SdC9876-'
ldapBaseDN="o=swift.com"
userFilesDir = './Resources/Generic'
RFUsers = {}
usersWithoutName=[]
for fn in [fn for fn in os.listdir(userFilesDir) if 'user' in fn]:
    with open(userFilesDir + '/' + fn,'r') as fhdl:
        pattern = re.compile(r'^\$\{(.*)\} +(.*)$')
        while 1:
            s = fhdl.readline()
            if not s: break
            m = re.match(pattern,s)
            if m:
                alias = m.group(1)
                userdata = m.group(2)
                user = '_'.join(alias.split('_')[:-1])
                if user not in RFUsers.keys():
                    RFUsers[user]={}
                if '_user' in alias:
                    RFUsers[user]['email']=userdata
                elif '_name' in alias:
                    names = userdata.split(' ')
                    RFUsers[user]['firstname']=names[0]
                    RFUsers[user]['lastname']=names[1]
                else:
                    pass
RFUserByGroup={}

for k,v in RFUsers.items():
    group =k.split('_')[1]
    if group[-1].isdigit():
        group = group[:-1]
    if group not in RFUserByGroup.keys():
        RFUserByGroup[group]={}
    RFUserByGroup[group][k]=v

pprint(RFUserByGroup)


##sdCIDMUsers = loadUserProfileFromLdap(RFUsers)
####print 'MISSING USERS:'
####for idmUser in sdCIDMUsers.values():
####    if not idmUser.profileIds and 'pac.kyc' in idmUser.email:
####        print  idmUser.firstName + '\t' + idmUser.lastName + '\t' +  idmUser.email + '\t' +  idmUser.swift2faIsMandatory + '\t' + idmUser.swift2faActivated
##print 'ALL KYC USERS USED IN RF:'
##for idmUser in sdCIDMUsers.values():
##    if 'pac.kyc' in idmUser.email: 
##        print  idmUser.firstName + '\t' + idmUser.lastName + '\t' +  idmUser.email + '\t' +  idmUser.swift2faIsMandatory + '\t' + idmUser.swift2faActivated + '\t' + idmUser.profileIds
