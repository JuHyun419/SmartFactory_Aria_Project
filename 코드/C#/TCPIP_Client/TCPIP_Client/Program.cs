using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace TCPIP_Client
{
    class Program
    {
        static void Main(string[] args)
        {
            if(args.Length < 4)
            {
                Console.WriteLine("사용법 : {0} <Bind IP> <Bind Port> <Server IP> <Message>", 
                    Process.GetCurrentProcess().ProcessName);
                return;
            }

            string bindIp = args[0];
            int bindPort = Convert.ToInt32(args[1]);    // 기본 데이터 형식을 다른 데이터 형식으로 변환
            string serverIp = args[2];
            const int serverPort = 5425;
            string message = args[3];

            try
            {
                IPEndPoint clientAddress = new IPEndPoint(IPAddress.Parse(bindIp), bindPort);
                IPEndPoint serverAddress = new IPEndPoint(IPAddress.Parse(serverIp), serverPort);

                //                                                지정된 끝점의 IP주소와 포트번호 반환
                Console.WriteLine("클라이언트 : {0}, 서버 : {1}", clientAddress.ToString(), serverAddress.ToString());
                TcpClient client = new TcpClient(clientAddress);

                // 지정된 네트워크의 끝점을 사용해 원격 TCP 호스트에 클라이언트 연결
                client.Connect(serverAddress);
                byte[] data = System.Text.Encoding.Default.GetBytes(message);
                NetworkStream stream = client.GetStream();
                stream.Write(data, 0, data.Length);
                Console.WriteLine("송신 : {0}", message);
                data = new byte[256];
                string responseData = "";
                int bytes = stream.Read(data, 0, data.Length);
                responseData = Encoding.Default.GetString(data, 0, bytes);
                Console.WriteLine("수신 : {0}", responseData);

                stream.Close();
                client.Close();
            }
            catch(SocketException e)
            {
                Console.WriteLine(e);
            }
            Console.WriteLine("클라이언트를 종료합니다.");


        }
    }
}
