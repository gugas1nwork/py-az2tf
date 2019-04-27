def azurerm_user_assigned_identity(crf,cde,crg,headers,requests,sub,json,az2tfmess,subprocess):
    # 015 user assigned identity
    tfp="azurerm_user_assigned_identity"
    azr=""
    if crf in tfp:
        p = subprocess.Popen('az identity list -o json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, errors = p.communicate()
        azr=json.loads(output)
        if cde:
            print(json.dumps(azr, indent=4, separators=(',', ': ')))

        tfrmf="015-"+tfp+"-staterm.sh"
        tfimf="015-"+tfp+"-stateimp.sh"
        tfrm=open(tfrmf, 'a')
        tfim=open(tfimf, 'a')
        print tfp,
        count=len(azr)
        print count
        for j in range(0, count):
            
            name=azr[j]["name"]
            loc=azr[j]["location"]
            id=azr[j]["id"]
            rg=azr[j]["resourceGroup"]

            if crg is not None:
                print "rgname=" + rg + " crg=" + crg
                if rg.lower() != crg.lower():
                    continue  # back to for
            
            rname=name.replace(".","-")
            prefix=tfp+"."+rg+'__'+rname
            #print prefix
            rfilename=prefix+".tf"
            fr=open(rfilename, 'w')
            fr.write("")
            fr.write('resource ' + tfp + ' ' + rg + '__' + rname + ' {\n')
            fr.write('\t name = "' + name + '"\n')
            fr.write('\t location = "'+ loc + '"\n')
            fr.write('\t resource_group_name = "' + rg + '"\n')
        # tags block
            try:
                mtags=azr[j]["tags"]
            except:
                mtags="{}"
            tcount=len(mtags)-1
            if tcount > 1 :
                fr.write('tags { \n')
                print tcount
                for key in mtags.keys():
                    tval=mtags[key]
                    fr.write('\t "' + key + '"="' + tval + '"\n')
                #print(json.dumps(mtags, indent=4, separators=(',', ': ')))
                fr.write('}\n')
            
            fr.write('}\n') 
            fr.close()  # close .tf file

            tfrm.write('terraform state rm '+tfp+'.'+rg+'__'+rname + '\n')
            
            tfcomm='terraform import '+tfp+'.'+rg+'__'+rname+' '+id+'\n'
            tfim.write('echo "importing ' + str(j) + ' of ' + str(count-1) + '"' + '\n')
            tfim.write(tfcomm)  

        # end for
        tfrm.close()
        tfim.close()
        #end user assigned identity