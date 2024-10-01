from app import *
from marshmallow import Schema, fields

class lessor_list(Schema):
   lessorname=fields.Str(default='')
   lessorfname=fields.Str(default='')
   lessoraddressline1=fields.Str(default='')
   lessoraddressline2=fields.Str(default='')
   lessorcitystatepincode=fields.Str(default='')

class leasee_list(Schema):
   lesseename=fields.Str(default='')
   lesseefname=fields.Str(default='')
   lesseeaddressline1=fields.Str(default='')
   lesseeaddressline2=fields.Str(default='')
   lesseecitystatepincode=fields.Str(default='')

class HRDRequest(Schema):
   lname= fields.Str(default="NY")
   tname=fields.Str(default="plate_type")
   address=fields.Str(dafault="10, ABC , Street-1 DEF-110003")
   leaseperiod=fields.Str(default="1 year")
   fromDt=fields.Str(default="1-09-2024")
   to=fields.Str(default="1-09-2024")
   monthlyrent=fields.Str(default="30000")
   deposit=fields.Str(default="100000") 
   #Below Schema is related to renting a mall drafting starting from City to witness2address
   city=fields.Str(default="city")
   day_montha=fields.Str(default="day_montha")
   year=fields.Str(default="year")
   lessor_list=fields.List(fields.Nested(lessor_list),required=True)
   leasee_list=fields.List(fields.Nested(leasee_list),required=True)
   address1=fields.Str(default="address1")
   address2=fields.Str(default="address2")
   leasepropertyaddress=fields.Str(default="leasepropertyaddress")
   leasepropertyarea=fields.Str(default="leasepropertyarea")
   leaseterm=fields.Str(default="leaseterm")
   leasedeedstartdate=fields.Str(default="leasedeedstartdate")
   leasedeedsigndate=fields.Str(default="leasedeedsigndate")
   leaseamount=fields.Str(default="leaseamount")
   monthlypaymentdate=fields.Str(default="monthlypaymentdate")
   twomonths=fields.Str(default="twomonths")
   onemonth=fields.Str(default="onemonth")


   witness1name=fields.Str(default="witness1name")
   witness2name=fields.Str(default="witness2name")
   witness1address=fields.Str(default="witness1address")
   witness2address=fields.Str(default="witness2address")


class Seller(Schema):
   seller_name=fields.Str(default='')
   seller_fathhus=fields.Str(default='')
   seller_age=fields.Str(default='')
   seller_pan=fields.Str(default='')
   seller_caste=fields.Str(default='')
   seller_address=fields.Str(default='')

class Purchaser(Schema):
   purchaser_name=fields.Str(default='')
   purchaser_father=fields.Str(default='')
   purchaser_age=fields.Str(default='')
   purchaser_caste=fields.Str(default='')
   purchaser_pan=fields.Str(default='')
   purchaser_address=fields.Str(default='')
   
class SDDRequest(Schema):
   username=fields.Str(default='')
   password=fields.Str(default='')
   day=fields.Str(default='')
   month=fields.Str(default='')
   year=fields.Str(default='')
   sellers=fields.List(fields.Nested(Seller),required=True)
   purchasers=fields.List(fields.Nested(Purchaser),required=True)
   type_of_property=fields.Str(default='')
   land=fields.Str(default='')
   land_size=fields.Str(default='')
   rs_plotnum=fields.Str(default='')
   lr_plotnum=fields.Str(default='')
   rs_khaitnanum=fields.Str(default='')
   lr_khaitannum=fields.Str(default='')
   moza=fields.Str(default='')
   jlnum=fields.Str(default='')
   touzinum=fields.Str(default='')
   policastation=fields.Str(default='')
   subdistrict=fields.Str(default='')
   district=fields.Str(default='')
   flatnumber=fields.Str(default='')
   floorno=fields.Str(default='')
   society=fields.Str(default='')
   division=fields.Str(default='')
   corporation=fields.Str(default='')
   road=fields.Str(default='')
   location=fields.Str(default='')
   supersqfeet=fields.Str(default='')
   landsqfeet=fields.Str(default='')
   percentage=fields.Str(default='')
   previous_owner=fields.Str(default='')
   father_previous_owner=fields.Str(default='')
   father_previous_owner_det=fields.Str(default='')
   previous_sale_deed=fields.Str(default='')
   reg_office=fields.Str(default='')
   volume=fields.Str(default='')
   frompage=fields.Str(default='')
   topage=fields.Str(default='')
   beingno=fields.Str(default='')
   year_prev_saledeed=fields.Str(default='')
   inestate=fields.Str(default='')
   seller_father_deathdate=fields.Str(default='')
   amount=fields.Str(default='')
   amount_in_words=fields.Str(default='')
   agreement_date=fields.Str(default='')
   recieved_money=fields.Str(default='')
   property_handover_date=fields.Str(default='')
   onNorth=fields.Str(default='')
   onSouth=fields.Str(default='')
   onEast=fields.Str(default='')
   onWest=fields.Str(default='')
   witness1=fields.Str(default='')
   witness2=fields.Str(default='')
   seller_type=fields.Str(default='')
   purchaser_type=fields.Str(default='')
   seller_builder_name=fields.Str(default='')
   seller_builder_reg_num=fields.Str(default='')
   seller_builder_fulladdress=fields.Str(default='')
   purchaser_builder_name=fields.Str(default='')
   purchaser_builder_reg_num=fields.Str(default='')
   purchaser_builder_fulladdress=fields.Str(default='')




class PSRRequest(Schema):
   agreement_date=fields.Str(default='')
   parking_amount=fields.Str(default='')
   effective_date=fields.Str(default='')
   seller_name=fields.Str(default='')
   lessor=fields.Str(default='')
   lessee=fields.Str(default='')
   parking_adress=fields.Str(default='')
   payment_method=fields.Str(default='')
   payment_day=fields.Str(default='')
   notice_period=fields.Str(default='')

class OSADRequest(Schema):
   day=fields.Str(default='')
   year=fields.Str(default='')
   Place_A=fields.Str(default='')
   place_B=fields.Str(default='')
   bearing_no=fields.Str(default='')
   situate_at=fields.Str(default='')
   period_of_month=fields.Str(default='')
   comming_from=fields.Str(default='')
   ending_on=fields.Str(default='')
   rupess=fields.Str(default='')
   rupess_in_words=fields.Str(default='')
   week_day=fields.Str(default='')
   date_of_day=fields.Str(default='')
   per_day=fields.Str(default='')
   per_anum=fields.Str(default='')
   deposite_rs=fields.Str(default='')
   deposite_rs_words=fields.Str(default='')
   signature_of_licensee=fields.Str(default='')
   abc_signature=fields.Str(default='')
   date_of_signature=fields.Str(default='')
   receipt_rs=fields.Str(default='')
   receipt_rs_in_words=fields.Str(default='')
   cheque_no=fields.Str(default='')
   cheque_dated=fields.Str(default='')
   cheque_branch=fields.Str(default='')
   witness1=fields.Str(default='')
   witness2=fields.Str(default='')


#One And The Same Person Affidavit
class SPARequest(Schema):
   name_real=fields.Str(default='')
   verification_state=fields.Str(default='')
   guardian_name=fields.Str(default='')
   verification_day=fields.Str(default='')
   name_2=fields.Str(default='')
   adress=fields.Str(default='')
   name_1=fields.Str(default='')
   relation=fields.Str(default='')

# Address Proof Affidavit
class APARequest(Schema):
   notary_public=fields.Str(default='')
   notary_country=fields.Str(default='')
   notary_state=fields.Str(default='')
   witness_2=fields.Str(default='')
   witness_1=fields.Str(default='')
   name=fields.Str(default='')
   state=fields.Str(default='')
   residency_start_date=fields.Str(default='')
   document_2=fields.Str(default='')
   document_1=fields.Str(default='')
   zip_code=fields.Str(default='')
   affidavit_date=fields.Str(default='')
   adress_line1=fields.Str(default='')
   city=fields.Str(default='')


class APIResponse(Schema):
   message=fields.String(default="")

