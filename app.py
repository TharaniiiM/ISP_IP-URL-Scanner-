from flask import Flask, render_template, request, url_for
import requests
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def abc():

    if request.method == 'POST':
        ip_address=request.form['firstname']

        headers = {
        "accept": "application/json",
        "x-apikey": "d0f2258cb348dd4d47b59f40e191e8003dbba66f15c1778eec0ec9462aa7558d"
        }
    
        response = requests.get( "https://www.virustotal.com/api/v3/ip_addresses/%s" %ip_address, headers=headers)
        outfromreq = response.json()["data"]["attributes"]["last_analysis_results"]

        #print(outfromreq)


        totalenginecount = 0
        totalenginesdetectedcount = 0
        resultengines = []
        enginenames = []
        test = []
            
        for i in outfromreq:
            totalenginecount = totalenginecount + 1
            if outfromreq[i]["category"] == "malicious" or outfromreq[i]["category"] == 'suspicious':
                resultengines.append(outfromreq[i]["result"])
                enginenames.append(outfromreq[i]["engine_name"])
                totalenginesdetectedcount = totalenginesdetectedcount + 1
            
        if totalenginesdetectedcount > 0:
            response_result = "The " + str(ip_address) + " is rated as unsafe on " + str(totalenginesdetectedcount) + " engines out of " + str(totalenginecount) + " engines."
            # return("The " + str(ip_address) + " is rated as unsafe on " + str(totalenginesdetectedcount) + " engines out of " + str(totalenginecount) + " engines.") 
            return render_template("result.html",result=response_result)
        elif totalenginesdetectedcount > -1:
            response_result ="The " + str(ip_address) + " is rated as Safe on " + str(totalenginecount) + " engines."
            # return("The " + str(ip_address) + " is rated as Safe on " + str(totalenginecount) + " engines." )
            # return render_template("test.html")
            return render_template("result.html",result=response_result)

        #print(request.form.get("firstname"))


    return render_template("index.html")



app.debug =True

app.run()