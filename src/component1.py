from flask import Flask, jsonify, request
import requests
import db2actions
import db2connection
import ibm_db
import validator
from exceptions import EnvInvException, PolicyInvException
import os
from loggingConfiguration import configureLogging

app= Flask(__name__)
app.config.from_Object("")
@app.route('/comp1')
def getComp1Details():
    try:
        param1=request.args["param1"]
        param2=request.args["param2"]
        authCheck= authenticate(request.headers)
        if authCheck:
          connect= db2Connection.getConnection(app.config, subsystem)
          result= db2act.getDetails(conn, databaseDetails)
          return jsonify(results), 200
        else:
          return authCheck.text, authCheck.status_code
    except EnvInvException:
        app.logger.error("EnvInvException", exc_info=True)
        return "EnvInvException", 400
     except KeyError:
        app.logger.error("KeyError", exc_info=True)
        return "KeyError", 400
     except exception as e:
        app.logger.error(e, exc_info=True)
        return "Internal server error", 400
        
  def authenticate(head) :
   return head
   
 if __name__=="__main__":
    app.run()
     
