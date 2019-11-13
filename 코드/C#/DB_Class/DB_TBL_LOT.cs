using MySql.Data.MySqlClient;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DB_Class
{
    class DB_TBL_LOT
    {
       
        public static string Lot_All_Info { get; set; }


        public static List<string> List_Lot_Id = new List<string>(); // _Id가 저장된 list
        public static List<string> List_Model_Id = new List<string>(); // model temp가 저장된 list
        public static List<string> List_Line_Id = new List<string>(); // model humidity가 저장된 list
        public static List<string> List_Total_Product_Count = new List<string>(); // model aname이 저장된 list
        public static List<string> List_Product_Speed_Warn = new List<string>(); // model 모든 컬럼 정보가 저장된 list
        public static List<string> List_Product_Fail_Rate_Warn = new List<string>(); // model 모든 컬럼 정보가 저장된 list
        public static List<string> List_Product_Color = new List<string>(); // model 모든 컬럼 정보가 저장된 list
        public static List<string> List_Temp_Margin = new List<string>(); // model 모든 컬럼 정보가 저장된 list
        public static List<string> List_Humid_Margin = new List<string>(); // model 모든 컬럼 정보가 저장된 list
        public static List<string> List_Oper_Id = new List<string>(); // model 모든 컬럼 정보가 저장된 list
        public static List<string> List_Working_State = new List<string>();
        public static List<string> List_Lot_Created_Time = new List<string>();
        public static List<string> List_Lot_Start_Time = new List<string>();
        public static List<string> List_Lot_End_Time = new List<string>();

        //public static string strconn = "Server=192.168.111.226;Database=Aria;Uid=root;Pwd=1234;"; // mysql 연동 변수
        //public static MySqlConnection conn = new MySqlConnection(DB_TBL_MODEL.strconn); // mysql 연결 함수 conn 정의


        // MySQL 연결 객체
        MySqlConnection conn;
        string strconn = "Server=192.168.111.226;Database=Aria;Uid=root;Pwd=1234;";

        // DB 연결
        public MySqlConnection getConnection()
        {
            conn = new MySqlConnection(strconn);
            conn.Open();
            return conn;
        }

        DB_TBL_LOT_DTO Dto = new DB_TBL_LOT_DTO();
        public void Lot_Insert(DB_TBL_LOT_DTO dB_TBL_LOT_DTO) // Lot 기본정보 Insert 메서드
        {
            conn = this.getConnection();
            
            // Lot_Insert
            string Lot_Insert_Sql = "INSERT INTO TBL_LOT (lot_id, model_id, line_id, total_product_count, product_speed_warn, product_fail_rate_warn, product_color, " +
                "temp_margin, humid_margin, oper_id, working_state, lot_created_time) VALUES('" + dB_TBL_LOT_DTO.Lot_Id+ "'," + dB_TBL_LOT_DTO.Model_Id + ",'" + dB_TBL_LOT_DTO.Line_Id + "'," +
                dB_TBL_LOT_DTO.Total_Product_Count+ "," + dB_TBL_LOT_DTO.Product_Speed_Warn+ ","+ dB_TBL_LOT_DTO.Product_Fail_Rate_Warn+ ", " +
                "'"+ dB_TBL_LOT_DTO.Product_Color + "'," + dB_TBL_LOT_DTO .Temp_Margin + "," + dB_TBL_LOT_DTO .Humid_Margin + ",'" + dB_TBL_LOT_DTO .Oper_Id + "'," + dB_TBL_LOT_DTO.Working_State + ",now());"; 
            MySqlCommand Command_Lot_Insert = new MySqlCommand(Lot_Insert_Sql, conn); // Insert Command문
            Command_Lot_Insert.ExecuteNonQuery(); // Insert 실행
            conn.Close(); // MySQL Close
        }

        public void Lot_Delete(DB_TBL_LOT_DTO dB_TBL_LOT_DTO) // Lot Delete 메서드
        {
            conn = this.getConnection();
            string Lot_Delete_Sql = "DELETE FROM TBL_LOT WHERE lot_id = " + dB_TBL_LOT_DTO.Lot_Id + ";"; // 
            MySqlCommand Command_Lot_Delete = new MySqlCommand(Lot_Delete_Sql, conn); // 
            Command_Lot_Delete.ExecuteNonQuery(); // 
            conn.Close(); // MySQL Close
        }

        public void Lot_Working_State_Update_0(DB_TBL_LOT_DTO dB_TBL_LOT_DTO) // Lot Working_State 상태 0 메서드
        {
            conn = this.getConnection();
            string Lot_Working_State_Update_Sql_0 = "UPDATE TBL_LOT SET working_state = 0 WHERE lot_id = '" + dB_TBL_LOT_DTO.Lot_Id + "';";
            MySqlCommand Command_Lot_Working_State_Update_0 = new MySqlCommand(Lot_Working_State_Update_Sql_0, conn);
            Command_Lot_Working_State_Update_0.ExecuteNonQuery();
            conn.Close();
        }

        public void Lot_Working_State_Update_1(DB_TBL_LOT_DTO dB_TBL_LOT_DTO) // Lot Working_State 상태 1 메서드
        {
            conn = this.getConnection();
            string Lot_Working_State_Update_Sql_1 = "UPDATE TBL_LOT SET working_state = 1 WHERE lot_id = '" + dB_TBL_LOT_DTO.Lot_Id + "';";
            MySqlCommand Command_Lot_Working_State_Update_1 = new MySqlCommand(Lot_Working_State_Update_Sql_1, conn);
            Command_Lot_Working_State_Update_1.ExecuteNonQuery();
            conn.Close();
        }

        public void Lot_Working_State_Update_2(DB_TBL_LOT_DTO dB_TBL_LOT_DTO) // Lot Working_State 상태 2 메서드
        {
            conn = this.getConnection();
            string Lot_Working_State_Update_Sql_2 = "UPDATE TBL_LOT SET working_state = 2 WHERE lot_id = '" + dB_TBL_LOT_DTO.Lot_Id + "';";
            MySqlCommand Command_Lot_Working_State_Update_2 = new MySqlCommand(Lot_Working_State_Update_Sql_2, conn);
            Command_Lot_Working_State_Update_2.ExecuteNonQuery();
            conn.Close();
        }

        public void Lot_Start_Time_Update(DB_TBL_LOT_DTO dB_TBL_LOT_DTO) // Lot Start Time Update 메서드
        {
            conn = this.getConnection();
            string Lot_Start_Time_Update_Sql = "UPDATE TBL_LOT SET lot_start_time = now() WHERE lot_id = '" + dB_TBL_LOT_DTO.Lot_Id + "';";
            MySqlCommand Command_Lot_Start_Time_Update = new MySqlCommand(Lot_Start_Time_Update_Sql, conn);
            Command_Lot_Start_Time_Update.ExecuteNonQuery();
            conn.Close();
        }

        public  void Lot_End_Time_Update(DB_TBL_LOT_DTO dB_TBL_LOT_DTO) // Lot End Time Update 메서드
        {
            conn = this.getConnection();
            string Lot_End_Time_Update_Sql = "UPDATE TBL_LOT SET lot_end_time = now() WHERE lot_id = '" + dB_TBL_LOT_DTO.Lot_Id + "';";
            MySqlCommand Command_Lot_End_Time_Update = new MySqlCommand(Lot_End_Time_Update_Sql, conn);
            Command_Lot_End_Time_Update.ExecuteNonQuery();
            conn.Close();
        }

        public void Lot_Select_All()
        {
            Lot_All_Info = "";
            List_Lot_Id.RemoveRange(0, List_Lot_Id.Count);
            List_Model_Id.RemoveRange(0, List_Model_Id.Count);
            List_Line_Id.RemoveRange(0, List_Line_Id.Count);
            List_Total_Product_Count.RemoveRange(0, List_Total_Product_Count.Count);
            List_Product_Speed_Warn.RemoveRange(0, List_Product_Speed_Warn.Count);
            List_Product_Fail_Rate_Warn.RemoveRange(0, List_Product_Fail_Rate_Warn.Count);
            List_Product_Color.RemoveRange(0, List_Product_Color.Count);
            List_Temp_Margin.RemoveRange(0, List_Temp_Margin.Count);
            List_Humid_Margin.RemoveRange(0, List_Humid_Margin.Count);
            List_Oper_Id.RemoveRange(0, List_Oper_Id.Count);
            List_Working_State.RemoveRange(0, List_Working_State.Count);
            List_Lot_Created_Time.RemoveRange(0, List_Lot_Created_Time.Count);
            List_Lot_Start_Time.RemoveRange(0, List_Lot_Start_Time.Count);
            List_Lot_End_Time.RemoveRange(0, List_Lot_End_Time.Count);

            conn = this.getConnection();
            string Lot_All_Select_Sql = "SELECT * FROM TBL_LOT;";//본인의 DB이름 
            MySqlCommand Command_Lot_All_Select = new MySqlCommand(Lot_All_Select_Sql, conn);
            MySqlDataReader Reader_Lot_All_Select = Command_Lot_All_Select.ExecuteReader(); // Sql문 Reader하는 Class
            ArrayList Lot_All_Select = new ArrayList(); // ArrayList 선언

            while (Reader_Lot_All_Select.Read()) // TBL_MODEL의 컬럼 내용 모두 읽을 때 까지 반복
            {
                //DB_TBL_LOT Lot_Select = new DB_TBL_LOT(); // TBL_MODEL 테이블 객체 생성
                DB_TBL_LOT_DTO Lot_Select = new DB_TBL_LOT_DTO();   // TBL_MODEL 테이블 객체 생성

                Lot_Select.Lot_Id =                 Reader_Lot_All_Select["lot_id"].ToString(); // TBL_MODEL 테이블의 model_id 컬럼 불러오기
                Lot_Select.Model_Id =               Reader_Lot_All_Select["model_id"].ToString(); // TBL_MODEL 테이블의 model_temp 컬럼 불러오기
                Lot_Select.Line_Id =                Reader_Lot_All_Select["line_id"].ToString(); // TBL_MODEL 테이블의 model_humidity 컬럼 불러오기
                Lot_Select.Total_Product_Count =    Reader_Lot_All_Select["total_product_count"].ToString(); // TBL_MODEL 테이블의 aname 컬럼 불러오기
                Lot_Select.Product_Speed_Warn =     Reader_Lot_All_Select["product_speed_warn"].ToString(); // TBL_MODEL 테이블의 model_id 컬럼 불러오기
                Lot_Select.Product_Fail_Rate_Warn = Reader_Lot_All_Select["product_fail_rate_warn"].ToString(); // TBL_MODEL 테이블의 model_temp 컬럼 불러오기
                Lot_Select.Product_Color =          Reader_Lot_All_Select["product_color"].ToString(); // TBL_MODEL 테이블의 model_humidity 컬럼 불러오기
                Lot_Select.Temp_Margin =            Reader_Lot_All_Select["temp_margin"].ToString(); // TBL_MODEL 테이블의 aname 컬럼 불러오기
                Lot_Select.Humid_Margin =           Reader_Lot_All_Select["humid_margin"].ToString(); // TBL_MODEL 테이블의 model_id 컬럼 불러오기
                Lot_Select.Oper_Id =                Reader_Lot_All_Select["oper_id"].ToString();
                Lot_Select.Working_State =          Reader_Lot_All_Select["working_state"].ToString();
                Lot_Select.Lot_Created_Time =       Reader_Lot_All_Select["lot_created_time"].ToString();
                Lot_Select.Lot_Start_Time =         Reader_Lot_All_Select["lot_start_time"].ToString();
                Lot_Select.Lot_End_Time =           Reader_Lot_All_Select["lot_end_time"].ToString();

                List_Lot_Id.Add(Lot_Select.Lot_Id); // 불러온 model_id 리스트에 담기
                List_Model_Id.Add(Lot_Select.Model_Id); // 불러온 model_temp 리스트에 담기
                List_Line_Id.Add(Lot_Select.Line_Id); // 불러온 model_humidity 리스트에 댐기
                List_Total_Product_Count.Add(Lot_Select.Total_Product_Count); // 불러온 aname 리스트에 담기
                List_Product_Speed_Warn.Add(Lot_Select.Product_Speed_Warn); // 불러온 model_id 리스트에 담기
                List_Product_Fail_Rate_Warn.Add(Lot_Select.Product_Fail_Rate_Warn); // 불러온 model_temp 리스트에 담기
                List_Product_Color.Add(Lot_Select.Product_Color); // 불러온 aname 리스트에 담기
                List_Temp_Margin.Add(Lot_Select.Temp_Margin); // 불러온 model_id 리스트에 담기
                List_Humid_Margin.Add(Lot_Select.Humid_Margin);
                List_Oper_Id.Add(Lot_Select.Oper_Id);
                List_Working_State.Add(Lot_Select.Working_State);
                List_Lot_Created_Time.Add(Lot_Select.Lot_Created_Time);
                List_Lot_Start_Time.Add(Lot_Select.Lot_Start_Time);
                List_Lot_End_Time.Add(Lot_Select.Lot_End_Time);

                Lot_All_Select.Add(Lot_Select); // 모든 정보 ArrayList 담기
            }
            int IndexA = 0;
            IEnumerator Lot_Array = Lot_All_Select.GetEnumerator(); // ArrayList를 반복 할 수 있도록 함.
            while (Lot_Array.MoveNext())
            {
                IndexA++;
                Object obj = Lot_Array.Current;
                //DB_TBL_LOT Lot_Select = (DB_TBL_LOT)obj;
                DB_TBL_LOT_DTO Lot_Select = (DB_TBL_LOT)obj;
                if (IndexA == Lot_All_Select.Count)
                {
                    Lot_All_Info = Lot_All_Info + Lot_Select.Lot_Id + "\t" + Lot_Select.Model_Id + "\t" + Lot_Select.Line_Id + "\t" + Lot_Select.Total_Product_Count + "\t" + Lot_Select.Product_Speed_Warn + "\t" + Lot_Select.Product_Fail_Rate_Warn + "\t" + Lot_Select.Product_Color + "\t" + Lot_Select.Temp_Margin + "\t" + Lot_Select.Humid_Margin + "\t" + Lot_Select.Oper_Id + "\t" + Lot_Select.Working_State + "\t" + Lot_Select.Lot_Created_Time + "\t" + Lot_Select.Lot_Start_Time + "\t" + Lot_Select.Lot_End_Time;
                }
                else
                {
                    Lot_All_Info = Lot_All_Info + Lot_Select.Lot_Id + "\t" + Lot_Select.Model_Id + "\t" + Lot_Select.Line_Id + "\t" + Lot_Select.Total_Product_Count + "\t" + Lot_Select.Product_Speed_Warn + "\t" + Lot_Select.Product_Fail_Rate_Warn + "\t" + Lot_Select.Product_Color + "\t" + Lot_Select.Temp_Margin + "\t" + Lot_Select.Humid_Margin + "\t" + Lot_Select.Oper_Id + "\t" + Lot_Select.Working_State + "\t" + Lot_Select.Lot_Created_Time + "\t" + Lot_Select.Lot_Start_Time + "\t" + Lot_Select.Lot_End_Time + "\n";
                }
            }

        }
        public static void Lot_Select(string lot_id)
        {
            string[] String_List_Lot_All = Lot_All_Info.Split(new char[] { '\n' }); // List_Model_All_Info 문자열을 , 기준으로 나누어서 배열에 적재

            int Index_i = 0; // foreach에서 증가값 변수
            int Index_e = 0; // 선택한 문자가 리스트의 몇번째인지 찾는 변수
            foreach (string number in List_Lot_Id) // Model_Id_Info 리스트 반복
            {
                if (number == lot_id) // 선택값과 User_id가 같은지 판단
                {
                    Index_e = Index_i; // 같을 시 Index_e에 Index_i값 저장
                }
                Index_i++; // Index_i 증가
            }
            Console.WriteLine(String_List_Lot_All[Index_e]); // 찾은 Index_e번째 리스트 불러오기
        }
    }
}
