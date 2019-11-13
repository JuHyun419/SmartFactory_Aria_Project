using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DB_Class
{
    /* DTO(Data Transfer Object)
     * - 데이터를 하나의 객체로 관리할 목적으로 만들어둔 클래스의 객체
     * - DTO들은 setter(), getter()를 가지고 직렬화 구현(Java 기준)
     * - C# = Property(프로퍼티 구현)
     */
    class DB_TBL_LOT_DTO
    {
        public string Lot_Id { get; set; }
        public string Model_Id { get; set; }
        public string Line_Id { get; set; }
        public string Total_Product_Count { get; set; }
        public string Product_Speed_Warn { get; set; }
        public string Product_Fail_Rate_Warn { get; set; }
        public string Product_Color { get; set; }
        public string Temp_Margin { get; set; }
        public string Humid_Margin { get; set; }
        public string Oper_Id { get; set; }
        public string Working_State { get; set; }
        public string Lot_Created_Time { get; set; }
        public string Lot_Start_Time { get; set; }
        public string Lot_End_Time { get; set; }

        /* static 필드(정적 필드) 
         *  - 프로그램 전체에 걸쳐 하나만 존재 
         *  - 프로그램 전체에 걸쳐 공유해야 하는 변수? --> 정적 필드 이용
         *  인스턴스(객체)를 만들지 않고 클래스의 이름을 통해 필드에 직접접근이 가능
         */
        public static string Lot_All_Info { get; set; }     // 모든 데이터들을 담을 변수

    }
}
