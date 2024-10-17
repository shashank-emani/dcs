import json
import os
import requests
from pyreportjasper import PyReportJasper


RESOURCES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources')
REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')


def generateReport(input_file,output_file,param,db_connection,username,password):
    try:
        input_file = os.path.join(REPORTS_DIR, input_file)
        output_file = os.path.join(REPORTS_DIR, output_file)
        pyreportjasper = PyReportJasper()
        pyreportjasper.config(
        input_file,
        output_file,
        output_formats=["pdf"],
        parameters= param,
        db_connection=db_connection)
            
        pyreportjasper.process_report()
        output_file = output_file + '.pdf'
        if os.path.isfile(output_file):
            print('Report generated successfully!')
            # Transfer the report to 
            print(type(output_file))
            try:
                with open(output_file, "rb") as file :
                    print(type(file))
                    response = requests.post(url="http://35.169.208.96:8000/api/document-management/upload/",files={"file":file},data={"username":"richa","password":"password"})
                    print(response.status_code)
                    data=response.json()
                    print(data['docnum'])
            except FileNotFoundError:
                print("The file was not found.")
            except requests.exceptions.RequestException as e:
                print("There was an exception that occurred while handling your request.", e)
    except Exception as e:
        print(str(e))
        raise e

def generateReport(input_file,output_file,param,db_connection):
    try:
        input_file = os.path.join(REPORTS_DIR, input_file)
        output_file = os.path.join(REPORTS_DIR, output_file)
        pyreportjasper = PyReportJasper()
        pyreportjasper.config(
        input_file,
        output_file,
        output_formats=["pdf"],
        parameters= param,
        db_connection=db_connection)
            
        pyreportjasper.process_report()
        output_file = output_file + '.pdf'
        if os.path.isfile(output_file):
            print('Report generated successfully!')
            # Transfer the report to 
            return output_file
    except Exception as e:
        print(str(e))
        raise e    
    
def getDbConnection(filename,party1key,party2key,listofparty1,listofparty2):
    json_file = os.path.join(RESOURCES_DIR, filename)
    f = open(json_file, "w")
    f.write("{\""+party1key+"\" : "+json.dumps(listofparty1)+",\""+party2key+"\" :"+json.dumps(listofparty2)+"}")
    f.close()
    db_connection=dict()
    db_connection['driver']='json'
    db_connection['data_file']= os.path.join(RESOURCES_DIR, filename)
    return db_connection