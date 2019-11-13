using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DB_Class
{
    class DB_TBL_LINE1
    {
        public string _Id { get; set; }
        public string Name { get; set; }
        public string State { get; set; }
        public string Working_Lot { get; set; }
        public string Line_Temp { get; set; }
        public string Line_Humidity { get; set; }
        public string Lot_Reserve { get; set; }
        public static string Line_All_Info { get; set; }

        public static List<string> List__Id = new List<string>();
        public static List<string> List_Name = new List<string>();
        public static List<string> List_State = new List<string>();
        public static List<string> List_Working_Lot = new List<string>();
        public static List<string> List_Line_Temp = new List<string>();
        public static List<string> List_Line_Humidity = new List<string>();
        public static List<string> List_Line_All_Info = new List<string>();

        public static string strconn = "Server=192.168.111.226;Database=Aria;Uid=root;Pwd=1234;"; // mysql 연동 변수
        public static MySqlConnection conn = new MySqlConnection(strconn); // mysql 연결 함수 conn 정의

        public static void Line1_Insert(string id, string name, string state, string working_lot, string line_temp, string line_humidity) // Model Insert 메소드
        {
            conn.Open(); // Mysql Open
            string Line1_Insert_Sql = "INSERT INTO TBL_LINE (_id, name, state, working_lot, line_temp, line_humidity) VALUES('" + id + "','" + name + "','" + state + "','" + working_lot + "','"+line_temp+"','"+line_humidity+"');"; // Insert 쿼리문
            MySqlCommand Command_Line1_Insert = new MySqlCommand(Line1_Insert_Sql, conn); // Insert Command문
            Command_Line1_Insert.ExecuteNonQuery(); // Insert 실행
            conn.Close(); // mysql Close
        }
        public static void Line1_Name_Update(string name, string change_name) // Model Update 메소드
        {
            conn.Open();
            string Line1_Name_Update_Sql = "update TBL_LINE set name = '" + change_name + "' where name = '" + name + "';";
            MySqlCommand Command_Line1_Name_Update = new MySqlCommand(Line1_Name_Update_Sql, conn);
            Command_Line1_Name_Update.ExecuteNonQuery();
            conn.Close();
        }
        public static void Model_Delete(string model_id) // Model Delete 메소드
        {
            conn.Open();
            string Model_Delete_Sql = "delete from TBL_MODEL where model_id = " + model_id + ";";
            MySqlCommand SQL_Delete = new MySqlCommand(Model_Delete_Sql, conn);
            SQL_Delete.ExecuteNonQuery();
            conn.Close();
        }
    }
}
