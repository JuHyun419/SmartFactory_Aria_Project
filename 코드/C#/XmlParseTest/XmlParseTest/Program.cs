using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml;

namespace XmlParseTest
{
    class Program
    {
        static void Main(string[] args)
        {
            //XmlDocument xdoc = new XmlDocument();

            //// XML 데이터를 파일에서 로드
            //xdoc.Load(@"C:\Temp\Aria.xml");

            //XmlNode emp1002 = xdoc.SelectSingleNode("/SECS2_XML_MESSAGE/HEAD[@Id='1001']");
            //Console.WriteLine(emp1002.InnerXml);

            //// 특정 노드 필터링
            //XmlNodeList nodes = xdoc.SelectNodes("SECS2_XML_MESSAGE/HEAD");

            //foreach (XmlNode emp in nodes)
            //{
            //    string id = emp.Attributes["Id"].Value;   // Attribute 읽기

            //    // 특정 자식 Element 읽기
            //    string SystemByte = emp.SelectSingleNode("SystemByte").InnerText;
            //    string CMD = emp.SelectSingleNode("CMD").InnerText;
            //    Console.WriteLine(id + "," + SystemByte + "," + CMD);


            //XmlNode emp1002 = xdoc.SelectSingleNode("/Employees/Employee[@Id='1002']");
            //Console.WriteLine(emp1002.InnerXml);



            XmlDocument xdoc = new XmlDocument();

            XmlNode root = xdoc.CreateElement("Employees");
            xdoc.AppendChild(root);

            // Emplyee #1001
            XmlNode emp1 = xdoc.CreateElement("Employee");
            XmlAttribute attr = xdoc.CreateAttribute("Id");
            attr.Value = "1001";
            emp1.Attributes.Append(attr);

            // <Name> </Name>
            XmlNode name1 = xdoc.CreateElement("Name");
            name1.InnerText = "Tim";
            emp1.AppendChild(name1);

            // <Dept> </Dept>
            XmlNode dept1 = xdoc.CreateElement("Dept");
            dept1.InnerText = "Sales";
            emp1.AppendChild(dept1);

            root.AppendChild(emp1);

            // Employee #1002
            var emp2 = xdoc.CreateElement("Employee");
            var attr2 = xdoc.CreateAttribute("Id");
            attr2.Value = "1002";
            emp2.Attributes.Append(attr2);

            // <Name> </Name>
            var name2 = xdoc.CreateElement("Name");
            name2.InnerText = "John";
            emp2.AppendChild(name2);

            // <Dept> </Dept>
            XmlNode dept2 = xdoc.CreateElement("Dept");
            dept2.InnerText = "HR";
            emp2.AppendChild(dept2);

            root.AppendChild(emp2);

            // XML 파일 저장
            xdoc.Save(@"C:\Temp\Emp2.xml");
            // ------------------------------------------


            XmlDocument xdoc = new XmlDocument();

            // XML 데이터를 파일에서 로드
            xdoc.Load(@"C:\Temp\Emp2.xml");

            // 특정 노드 필터링
            XmlNodeList nodes = xdoc.SelectNodes("/Employees/Employee");
            foreach (XmlNode emp in nodes)
            {
                // Attribute 읽기
                string id = emp.Attributes["Id"].Value;

                // 특정 자식 Element 읽기
                string name = emp.SelectSingleNode("Name").InnerText;
                string dept = emp.SelectSingleNode("Dept").InnerText;
                Console.WriteLine(id + "," + name + "," + dept);


                // 자식 노드들에 대해 Loop 도는 예시
                foreach (XmlNode child in emp.ChildNodes)
                {
                    Console.WriteLine("{0} : {1}", child.Name, child.InnerText);
                }
            }

          }
        }
    }


