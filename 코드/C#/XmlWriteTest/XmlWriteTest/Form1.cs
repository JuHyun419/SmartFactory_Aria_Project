using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml;

namespace XmlWriteTest
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // XML 파일 쓰기
        private void Btn_XmlWrite_Click(object sender, EventArgs e)
        {
            XmlDocument xdoc = new XmlDocument();

            XmlNode root = xdoc.CreateElement("SECS2_XML_MESSAGE");
            xdoc.AppendChild(root);

            // <HEAD> </HEAD>
            XmlNode head = xdoc.CreateElement("HEAD");
            XmlAttribute attr = xdoc.CreateAttribute("Id");
            attr.Value = "01";
            head.Attributes.Append(attr);

            // <SystemByte> </SystemByte>
            XmlNode systemByte = xdoc.CreateElement("SystemByte");
            systemByte.InnerText = txt_SystemByte.Text;
            head.AppendChild(systemByte);

            // <CMD> </CMD>
            XmlNode cmd = xdoc.CreateElement("CMD");
            cmd.InnerText = txt_CMD.Text;
            head.AppendChild(cmd);

            // <Stream> </Stream>
            XmlNode stream = xdoc.CreateElement("Stream");
            stream.InnerText = txt_Stream.Text;
            head.AppendChild(stream);

            // <Function> </Function>
            XmlNode function = xdoc.CreateElement("Function");
            function.InnerText = txt_Function.Text;
            head.AppendChild(function);
            root.AppendChild(head);

            // <BODY> </BODY>
            XmlNode body = xdoc.CreateElement("BODY");
            XmlAttribute attr2 = xdoc.CreateAttribute("Id");
            attr2.Value = "02";
            body.Attributes.Append(attr2);

            // <HCACK> </HCACK>
            XmlNode hcack = xdoc.CreateElement("HCACK");
            hcack.InnerText = txt_HCACK.Text;
            body.AppendChild(hcack);
            root.AppendChild(body);

            // XML 파일 저장
            xdoc.Save(@"C:\Temp\Aria3.xml");
        }

        // XML 파일 읽기
        private void Btn_XmlRead_Click(object sender, EventArgs e)
        {
            XmlDocument xdoc = new XmlDocument();

            // XML 데이터를 파일에서 로드
            xdoc.Load(@"C:\Temp\Aria.xml");

            // 특정 노드 필터링
            XmlNodeList nodes = xdoc.SelectNodes("/SECS2_XML_MESSAGE/HEAD");
            
            // XmlNodeList 객체 반복문
            foreach(XmlNode head in nodes)
            {
                // Attribute 읽기
                string id = head.Attributes["Id"].Value;

                // 특정 자식 Element 읽기
                string systemByte = head.SelectSingleNode("SystemByte").InnerText;
                string cmd = head.SelectSingleNode("CMD").InnerText;
                string stream = head.SelectSingleNode("Stream").InnerText;
                string function = head.SelectSingleNode("Function").InnerText;
                richTextBox1.Text = id + "\n" 
                    + systemByte + "\t" 
                    + cmd + "\t" 
                    + stream + "\t" 
                    + function;
            }
        }
    }
}
