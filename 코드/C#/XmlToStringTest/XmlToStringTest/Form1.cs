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

/* 다음 형식의 XML 파일 작성
 <?xml version="1.0" encoding="utf-8"?>
<Students>
  <Student Number="1" Name="김동영">
    <Score>
      <Korean>10</Korean>
      <English>20</English>
      <Math>30</Math>
      <Science>40</Science>
      <Music>50</Music>
      <Art>60</Art>
    </Score>
  </Student>
</Students>
 */

namespace XmlToStringTest
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            string url = @"C:\Temp\Aria.xml";
            try
            {
                XmlDocument xml = new XmlDocument();
                xml.Load(url);  // XML 파일 불러오기
                XmlNodeList xnList = xml.SelectNodes("/SECS2_XML_MESSAGE/HEAD"); // 접근할 노드
                
                foreach(XmlNode xn in xnList)
                {
                    // XML 파일 각각의 Element 불러오기
                    string SystemByte = xn["SystemByte"].InnerText;
                    string CMD = xn["CMD"].InnerText;
                    string Stream = xn["Stream"].InnerText;
                    string Function = xn["Function"].InnerText;
                    richTextBox1.AppendText(SystemByte + "\n" + CMD + "\n" + Stream + "\n" + Function);
                }

            }
            catch(ArgumentException ex)
            {
                MessageBox.Show(ex.ToString());
            }
        }
    }
}




