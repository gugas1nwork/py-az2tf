# azurerm_cosmosdb_account
def azurerm_cosmosdb_account(crf,cde,crg,headers,requests,sub,json,az2tfmess):
    tfp="azurerm_cosmosdb_account"
    tcode="400-"
    azr=""
    if crf in tfp:
    # REST or cli
        print "REST Managed Disk"
        url="https://management.azure.com/subscriptions/" + sub + "/providers/Microsoft.Compute/disks"
        params = {'api-version': '2017-03-30'}
        r = requests.get(url, headers=headers, params=params)
        azr= r.json()["value"]
        if cde:
            print(json.dumps(azr, indent=4, separators=(',', ': ')))

        tfrmf=tcode+tfp+"-staterm.sh"
        tfimf=tcode+tfp+"-stateimp.sh"
        tfrm=open(tfrmf, 'a')
        tfim=open(tfimf, 'a')
        print tfp,
        count=len(azr)
        print count
        for i in range(0, count):

            name=azr[i]["name"]
            loc=azr[i]["location"]
            id=azr[i]["id"]
            rg=id.split("/")[4].replace(".","-")

            if crg is not None:
                if rg.lower() != crg.lower():
                    continue  # back to for
            
            rname=name.replace(".","-")
            prefix=tfp+"."+rg+'__'+rname
            #print prefix
            rfilename=prefix+".tf"
            fr=open(rfilename, 'w')
            fr.write(az2tfmess)
            fr.write('resource ' + tfp + ' ' + rg + '__' + rname + ' {\n')
            fr.write('\t name = "' + name + '"\n')
            fr.write('\t location = "'+ loc + '"\n')
            fr.write('\t resource_group_name = "'+ rg + '"\n')

    ###############
    # specific code start
    ###############



azr=az cosmosdb list -g rgsource -o json
count= azr | | len(
if count > 0" :
    for i in range(0,count):
        
        name=azr[i]["name"]
        rname= name.replace(".","-")
        rg=azr[i]["resourceGroup"].replace(".","-")

        id=azr[i]["id"]
        loc=azr[i]["location"
        kind=azr[i]["kind"]
        offer=azr[i]["databaseAccountOfferType"]
        cp=azr[i]["consistencyPolicy.defaultConsistencyLevel"]
        mis=azr[i]["consistencyPolicy.maxIntervalInSeconds"]
        msp=azr[i]["consistencyPolicy.maxStalenessPrefix"] 
        caps=azr[i]["capabilities[0]["name"] 
        geol=azr[i]["failoverPolicies"       
        
        af=azr[i]["enableAutomaticFailover"]      
        
        fr.write('resource "' +  "' + '__' + "' {' tfp rg rname + '"\n')
        fr.write('\t name = "' +  name + '"\n')
        fr.write('\t location =  "loc" + '"\n')
        fr.write('\t resource_group_name = "' +  rgsource + '"\n')
        fr.write('\t kind = "' +  kind + '"\n')
        fr.write('\t offer_type = "' +  offer + '"\n')
        fr.write('\t consistency_policy {'  + '"\n')
        fr.write('\t\t  consistency_level = "' +  cp + '"\n')
        fr.write('\t\t  max_interval_in_seconds = "' +  mis + '"\n')
        fr.write('\t\t  max_staleness_prefix = "' +  msp + '"\n')
        fr.write('\t }' offer + '"\n')
        fr.write('\t enable_automatic_failover = "' +  af + '"\n')
# capabilities block

        # code out terraform error
        if caps" = "EnableTable" ]["|| [ "caps" = "EnableGremlin" ]["|| [ "caps" = "EnableCassandra" ]["; :
        fr.write('\t capabilities {'  + '"\n')

        fr.write('\t\t name = "' +  caps + '"\n')        
        fr.write('\t }' caps + '"\n')
       
# geo location block
        
        icount= geol | | len(
        if icount > 0" :
            for j in range(0,icount):
                floc=azr[i]["failoverPolicies[j]["locationName"
                fop=azr[i]["failoverPolicies[j]["failoverPriority"]
                fr.write('\t geo_location {'   + '"\n')
                fr.write('\t location =    "floc" + '"\n')
                fr.write('\t failover_priority  = "' +    fop + '"\n')
                fr.write('}\n')
            
          
        
        fr.write('}\n')
        #

        cat outfile

    
fi

    ###############
    # specific code end
    ###############

    # tags block       
            try:
                mtags=azr[i]["tags"]
                fr.write('tags { \n')
                for key in mtags.keys():
                    tval=mtags[key]
                    fr.write('\t "' + key + '"="' + tval + '"\n')
                fr.write('}\n')
            except KeyError:
                pass

            fr.write('}\n') 
            fr.close()   # close .tf file

            if cde:
                with open(rfilename) as f: 
                    print f.read()

            tfrm.write('terraform state rm '+tfp+'.'+rg+'__'+rname + '\n')

            tfim.write('echo "importing ' + str(i) + ' of ' + str(count-1) + '"' + '\n')
            tfcomm='terraform import '+tfp+'.'+rg+'__'+rname+' '+id+'\n'
            tfim.write(tfcomm)  

        # end for i loop

        tfrm.close()
        tfim.close()
    #end stub