using MySql.Data.MySqlClient;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;

using System.Threading.Tasks;

namespace serserser
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                sokets start = new sokets();
            }
            catch (System.IndexOutOfRangeException j)
            {
                Console.WriteLine(j);
            }
        }
    }
    class user
    {
        public static string id { set; get; }
        public static string pw { set; get; }
        public static string just { set; get; }
        public string nnd { set; get; }
    }

    // DB 테이블 컬럼
    class USERS
    {
        public string user_id { set; get; }
        public string pass_word { set; get; }
        public string level { set; get; }
        public string e_mail { set; get; }
        public string first_name { set; get; }
        public string last_name { set; get; }
    }
    class sokets
    {
        public sokets()
        {
            string bintIp = "220.69.249.231";   // Server IP
            const int bindPort = 8037;          // 임의의 포트 지정

            // TCP 네트워크 클라이언트에서 연결에 대한 수신 대기
            TcpListener server = null;

            //서버주소 바인딩(ip번호, port번호)
            string a, b, d;
            IPEndPoint localAddress = new IPEndPoint(IPAddress.Parse(bintIp), bindPort);    // Server IP

            //서버 만들기, 주소바인딩~!!!
            server = new TcpListener(localAddress); // TCP 네트워크 클라이언트의 연결 수신

            server.Start();
            Console.WriteLine("ARIA 프로젝트 서버");

            while (true)
            {
                // TCP 네트워크 서비스에 대한 클라이언트 연결 제공
                TcpClient client = server.AcceptTcpClient();    // 보류중인 연결요청 수락

                // 원격 엔드포인트를 가져옴
                ((IPEndPoint)client.Client.RemoteEndPoint).ToString();

                // 네트워크 액세스에 대한 데이터의 내부 스트림 제공
                // 읽기, 쓰기를 위한 클라이언트 스트림 받기
                NetworkStream stream = client.GetStream();

                int length;
                string data = null;
                byte[] bytes = new byte[256];

                // Read() --> NetworkStream으로 부터 데이터를 읽고, byte 배열에 저장
                length = stream.Read(bytes, 0, bytes.Length);

                data = Encoding.Default.GetString(bytes, 0, length);    // 데이터 수신
                Console.WriteLine(string.Format("수신 : {0} ", data));
                a = string.Format(data);    // 객체의 값을 문자열로 변환
                b = a.Substring(0, 4);
                string[] c = a.Split(new char[] { ',' });

                // 예외처리
                try
                {
                    // Aria 프로토콜 
                    if (b == "{#!!")
                    {
                        login l = new login();
                        user.id = c[1];
                        user.pw = c[2];
                        string e = l.log_in(user.id, user.pw);
                        byte[] msg = Encoding.Default.GetBytes(e); //
                        stream.Write(msg, 0, msg.Length);   // 데이터 송신
                        Console.WriteLine(string.Format("송신 : {0} ", e));
                    }
                }
                catch (System.IndexOutOfRangeException j)
                {
                    Console.WriteLine(j);
                }

            }
        }
    }

    /// <summary>
    /// Login Class
    /// </summary>
    class login
    {
        public string log_in(string b, string c)
        {
            string e;
            MySqlConnection conn;

            // MySQL 연결 변수
            string strconn = "Server=192.168.111.226;Database=Aria;Uid=root;Pwd=1234;";
            conn = new MySqlConnection(strconn);
            conn.Open();
            string strSelect = "SELECT * FROM users;";  // 본인의 DB 계정 
            MySqlCommand cmd = new MySqlCommand(strSelect, conn);
            MySqlDataReader rdr = cmd.ExecuteReader();

            string[,] arr = new string[1000, 2]; // 아이디와 비밀번호를 담을 2차원 배열
            int id_num = 0; // 아이디배열 증가 index
            int pw_num = 0; // 비일번호배열 증가 index
            StringBuilder sb = new StringBuilder();
            ArrayList user_all = new ArrayList(); // users 테이블의 값들이 담길 arraylist

            int aa = 0;
            user uu = new user();
            while (rdr.Read())
            {
                int bb = 0;
                USERS aria_user_data = new USERS();
                pw_num = 0;
                arr[id_num, pw_num] = rdr["user_id"].ToString();
                pw_num = 1;
                arr[id_num, pw_num] = rdr["pass_word"].ToString();
                id_num++;
                user_all.Add(aria_user_data);
                if (arr[aa, bb] == b && arr[aa, bb + 1] == c)
                {
                    uu.nnd = "정답입니다!";
                }
                aa++;
            }
            return uu.nnd;
        }
    }
}