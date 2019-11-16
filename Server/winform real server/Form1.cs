using MySql.Data.MySqlClient;
using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
//이게진짜
namespace winform_real_server
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            Server server = new Server(this);
            Thread c = new Thread(server.Server_Open);
            c.IsBackground = true;
            c.Start();

        }
            private void Form1_Load(object sender, EventArgs e)
        {

        }
        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void TextBox2_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
