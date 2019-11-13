using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace winform_real_server
{
    class Receive_User
    {
        public string User_All_select(string send_data)
        {
            List<DB_USERS> User = new List<DB_USERS>();
            DB_MGR.Users_Select(ref User);
            int a = 0;
            foreach (DB_USERS ee in User)
            {
                a++;
                if (User.Count == a)
                {
                    send_data = send_data + ee.User_Id + "," + ee.Pass_Word + "," + ee.Level + "," + ee.E_Mail + "," +
                        ee.First_Name + "," + ee.Last_Name;
                }
                else
                {
                    send_data = send_data + ee.User_Id + "," + ee.Pass_Word + "," + ee.Level + "," + ee.E_Mail + "," +
                        ee.First_Name + "," + ee.Last_Name + ",\n";
                }
            }
            return send_data;
        }
        public string User_select(string send_data, string receive_data_division)
        {
            List<DB_USERS> User = new List<DB_USERS>();
            DB_MGR.Users_Select(ref User);

            foreach (DB_USERS ee in User)
            {
                if (receive_data_division == ee.User_Id)
                {
                    send_data = ee.User_Id + "," + ee.Pass_Word + "," + ee.Level + "," + ee.E_Mail + "," +
                        ee.First_Name + "," + ee.Last_Name;
                }
            }
            return send_data;
        }
        public void User_update()
        {

        }
        public void User_delete()
        {

        }
    }
}
