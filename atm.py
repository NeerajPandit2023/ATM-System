import mysql.connector as ms
mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='atm_data')
mycur=mydb.cursor()
mycur.execute('Select pin from cos_data')
write=mycur.fetchall()
for l in range(100):
    print('\t\t\tWelcome in Bank of India\n\t\t\tInsert your Debit card details.')
    pin=int(input('Enter your pin: '))
    for i in write:
        z=i[0]
        if z==pin:
            cdb=mydb.cursor()
            cdb.execute(f'Select * from cos_data where pin={z}')
            info=cdb.fetchone()
            hideac=f"xxxxxx{info[0][-5:]}"
            print(f"Hi {info[1]}, Your A/c is {hideac} and your Avl_bal Rs.{info[3]}.")
            for k in range(5):
                c=input('choose your tarnsaction\n1. Withdraw\n2. Balance enqueiry\n3. fast cash\n4. Credit Amount\n: ')
                if c=='1':
                    x=int(input('Enter your widthdraw amount: '))
                    cdb=mydb.cursor()
                    cdb.execute(f'Select balance from cos_data where pin={z}')
                    info=cdb.fetchone()
                    n=info[0]
                    if (n==x or n>x) and x%100==0:
                        adb=mydb.cursor()
                        ubal=n-x
                        adb.execute(f'update cos_data set balance={ubal} where pin={z}')
                        mydb.commit()
                        print('Thank you for transaction')
                        print('Please collect cash And Debit Card')
                    elif x%100!=0:
                        print("Incorrect Ammount.")
                    else:
                        print('>>>Tu garib hai. ! sorry can\'t your withdraw amount\nyour available balance is',n,'only & So you can exit transaction')
                    if k!=4:
                        x2=input('If you want to check more operation (yes/no): ')
                        if x2=='no':
                            break
                elif c=='2':
                    cbal=mydb.cursor()
                    cbal.execute(f'Select balance from cos_data where pin={z}')
                    info=cbal.fetchone()
                    n=info[0]
                    print('Available balance is',n)
                    if k!=4:
                        x2=input('If you want to check more operation (yes/no): ')
                        if x2=='no':
                            break
                elif c=='3':
                    f=int(input('choose amount 1-1000, 2-500, 3-2000, 4,5000 : '))
                    acdb=mydb.cursor()
                    acdb.execute(f'select balance from cos_data where pin={z}')
                    info=acdb.fetchone()
                    k=info[0]
                    if f==1 and k>f:
                        adb=mydb.cursor()
                        uba=k-1000
                        adb.execute(f'update cos_data set balance={uba} where pin={z}')
                        mydb.commit()
                        print('Take cash 1000')
                    elif f==2 and k>f:
                        adb=mydb.cursor()
                        uba=k-500
                        adb.execute(f'update cos_data set balance={uba} where pin={z}')
                        mydb.commit()
                        print('Take cash 500')
                    elif f==3 and k>f:
                        adb=mydb.cursor()
                        uba=k-2000
                        adb.execute(f'update cos_data set balance={uba} where pin={z}')
                        mydb.commit()
                        print('Take cash 2000')
                    elif f==4 and k>f:
                        adb=mydb.cursor()
                        uba=k-5000
                        adb.execute(f'update cos_data set balance={uba} where pin={z}')
                        mydb.commit()
                        print('Take cash 5000')
                    else:
                        print('please choose amount.')
                    if k!=4:
                        x2=input('If you want to check more operation (yes/no): ')
                        if x2=='no':
                            break
                elif c=='4':
                    add_amt=int(input('Enter Credit amount: '))
                    Add_bal=mydb.cursor()
                    Add_bal.execute(f'Select balance from cos_data where pin={z}')
                    Add_c=Add_bal.fetchone()
                    o=Add_c[0]
                    avl_bal=add_amt+o
                    bsql=f"update cos_data set balance={avl_bal} where pin={z}"
                    Add_bal.execute(bsql)
                    mydb.commit()
                    print(f"Credited Rs.{add_amt}. And Your Avl Bal Rs.{avl_bal}.")
                    if k!=4:
                        x2=input('If you want to check more operation (yes/no): ')
                        if x2=='no':
                            break
                else:
                    print('pls choose tansaction.')
            else:
                print('>>>> !! Something went worng! you are done more transaction! So stop here.')
                break
    else:
        print('worng card pin >> Remove card Please !!')
else:
    print("Today's over transcation")