def CountofCyberBreachesperState(b_report):
    sv = b_report.State.value_counts().reset_index()
    sv.rename(columns={'index':'State', 'State':'Count of Breaches per State'}, inplace=True)
    return sv

def TypeofBreach(b_report):
    tpb = b_report['Type of Breach'].value_counts().reset_index()
    tpb.rename(columns={'index':'Type of Breach', 'Type of Breach':'Count of Types of Breaches that have Occurred'}, inplace=True)
    return tpb

def CoveredEntityType(b_report):
    cet = b_report['Covered Entity Type'].value_counts().reset_index()
    cet.rename(columns={'index':'Covered Entity Type', 'Covered Entity Type':'Count of Types of Breaches per Entity Type'}, inplace=True)
    return cet

def LocationofBreachedInformation(b_report):
    lb = b_report['Location of Breached Information'].value_counts().reset_index()
    lb.rename(columns={'index':'Location of Breached Information', 'Location of Breached Information':'Count of where Breaches have Occured'}, inplace=True)
    return lb

def BusinessAssociatePresent(b_report):
    bap = b_report['Business Associate Present'].value_counts().reset_index()
    bap.rename(columns={'index':'Business Associate Present', 'Business Associate Present':'Count of Presence of Business Associate'}, inplace=True)
    return bap

def NameofCoveredEntityperStateperBusinessAssociatePresent(b_report):
    return b_report.groupby(['Name of Covered Entity','State'])['Business Associate Present'].sum().reset_index()

def  LocationofBreachedInformationBreachSubmissionDateTypeofBreach(b_report):
    return b_report.groupby(['Location of Breached Information', 'Breach Submission Date'])['Type of Breach'].sum().reset_index()

def NameofCoveredEntityCoveredEntityTypeState(b_report):
    return b_report.groupby(['Name of Covered Entity', 'Covered Entity Type'])['State'].sum().reset_index()