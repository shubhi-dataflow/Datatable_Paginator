from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from app1.models import *
import psycopg2

# Create your views here.

def index(request):
    print("inside index")
    return render(request, 'index.html')


# def ajaxfile(request):
#     try:
#         # conn = mysql.connect()
#         # cursor = conn.cursor(pymysql.cursors.DictCursor)

#         conn = psycopg2.connect(
#           database="hospital_db", user='analytics', password='analytics@123', host='ec2-46-137-142-6.eu-west-1.compute.amazonaws.com', port= '5432'   )
#         cursor = conn.cursor()
#         print("connection establised")

#         if request.method == 'POST':
#             draw = request.form['draw']
#             row = int(request.form['start'])
#             rowperpage = int(request.form['length'])
#             searchValue = request.form["search[value]"]
#             print(draw)
#             print(row)
#             print(rowperpage)
#             print(searchValue)
 
#             ## Total number of records without filtering
#             cursor.execute("select count(*) as allcount from bed_capacity")
#             rsallcount = cursor.fetchone()
#             totalRecords = rsallcount['allcount']
#             print(totalRecords) 
 
#             ## Total number of records with filtering
#             likeString = "%" + searchValue +"%"
#             cursor.execute("SELECT count(*) as allcount from bed_capacity WHERE Address LIKE %s OR City LIKE %s OR State LIKE %s", (likeString, likeString, likeString))
#             rsallcount = cursor.fetchone()
#             totalRecordwithFilter = rsallcount['allcount']
#             print(totalRecordwithFilter) 
 
#             ## Fetch records
#             if searchValue=='':
#                 cursor.execute("SELECT * FROM bed_capacity ORDER BY Address asc limit %s, %s;", (row, rowperpage))
#                 bed_capacitylist = cursor.fetchall()
#             else:        
#                 cursor.execute("SELECT * FROM bed_capacity WHERE Address LIKE %s OR City LIKE %s OR State LIKE %s limit %s, %s;", (likeString, likeString, likeString, row, rowperpage))
#                 bed_capacitylist = cursor.fetchall()
 
#             # data = []
#             data={}
#             # for row in bed_capacitylist:
#             #     data.append({
#             #         'name': row['Address'],
#             #         'position': row['City'],
#             #         'age': row['State'],
#             #         'salary': row['salary'],
#             #         'office': row['office'],
#             #     })
#             for row in bed_capacitylist:

#                     data['name'] = row['Address'],
#                     data['position']= row['City'],
#                     data['age']= row['State'],
#                     data['salary']= row['salary'],
#                     data['office'] = row['office'],
        
 
#             response = {
#                 'draw': draw,
#                 'iTotalRecords': totalRecords,
#                 'iTotalDisplayRecords': totalRecordwithFilter,
#                 'aaData': data,
#             }
#             # return JsonResponse(response, safe=False)
#             return JsonResponse(data, safe=False)
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close() 
#         conn.close()
#         print("closed")


def ajaxfile(request):
    print("#################################")
    print(request.POST)
    try:
        conn = psycopg2.connect(
        database="hospital_db", user='analytics', password='analytics@123', host='ec2-46-137-142-6.eu-west-1.compute.amazonaws.com', port= '5432')
        cursor = conn.cursor()
        print("connection establised")
        if request.method == 'GET':
            print("inside if")
            draw = request.GET['draw']
            row = int(request.GET['start'])
            rowperpage = int(request.GET['length'])
            searchValue = request.GET["search[value]"]
            print("draw-",draw)
            print("row-",row)
            print("rowperpage-",rowperpage)
            print("searchValue-",searchValue)

            cursor.execute("Select * FROM bed_capacity LIMIT 0")
            colnames = [desc[0] for desc in cursor.description]
            print("colnames--",colnames)

            # cursor.execute('Select "City" from bed_capacity')

            # Total number of records without filtering
            cursor.execute("select count(*) as allcount from bed_capacity")
            rsallcount = cursor.fetchone()
            totalRecords = rsallcount[0]
            print("totalRecords",totalRecords)

            # Total number of records with filtering
            likeString = "%" + searchValue +"%"
            cursor.execute("""SELECT count(*) as allcount from bed_capacity WHERE "Name of Hospital" LIKE %s OR "Address" LIKE %s OR "City" LIKE %s""", (likeString, likeString, likeString))
            rsallcount = cursor.fetchone()
            totalRecordwithFilter = rsallcount[0]
            print("totalRecordwithFilter",totalRecordwithFilter)

            # Fetch records
            if searchValue=='':
                cursor.execute("SELECT * FROM bed_capacity OFFSET %s  limit %s;", (row, rowperpage))
                bed_capacitylist = cursor.fetchall()
                print("inside if searchValue=='':")

            else:
                cursor.execute("""Select * from bed_capacity WHERE "Name of Hospital" LIKE %s OR "Address" LIKE %s OR "City" LIKE %s ORDER BY "City" asc OFFSET %s  limit %s """, (likeString, likeString, likeString, row, rowperpage))
                bed_capacitylist = cursor.fetchall()
                # cursor.execute("SELECT * FROM bed_capacity WHERE 'Name of Hospital' LIKE %s OR 'Address' LIKE %s OR 'City' LIKE %s OFFSET %s limit %s;", (likeString, likeString, likeString, row, rowperpage))
            
            data = []
            for row in bed_capacitylist:
                data.append({

                            'id': row[0],
                            'name': row[1],
                            'position': row[2],
                            'age': row[3],
                            'salary': row[4],
                            'office': row[5],
                            'Contact no.': row[6],
                            'Email': row[7],
                            'Number of Doctors': row[8],
                            'Number of Nurses': row[9],
                            'Number of Beds': row[10],
                            'Number of ICU Beds': row[11],
                            'Available Departments': row[12],
                            'Source': row[13]
                    
                            })
            response = {
                    'draw': draw,
                    'iTotalRecords': totalRecords,
                    'iTotalDisplayRecords': totalRecordwithFilter,
                    'aaData': data,
            }
            return JsonResponse(response, safe=False)

    except Exception as e:
        print("ERROR",e)

    finally:
        cursor.close() 
        conn.close()
        print("closed")

    return HttpResponse("<p> Function returns DB connection errors.</p>")


