using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MES_Com_Demo
{
    public class CJobInfo
    {
        public string sLotId;
        public string sModel;
        public int nTotalProdCount;
    }

    public class CRasberryPiCom
    {
        public int Send_Work_Job(CJobInfo _Job_Info)
        {
            return 0;
        }
    }

    public class CMESClientCom
    {
        public int recv_req_user_login(string _id, string _pw)
        {
            return 0;
        }

        public int send_req_user_login_ack(string _sResult, string _sRignt, string _nak_reason)
        {
            return 0;
        }
    }

    public partial class fmMain : Form
    {
        CRasberryPiCom m_RPCom;
        CMESClientCom m_ClientCom;
        public fmMain()
        {
            InitializeComponent();
        }

        private void Recive_MES_Client_Req_User_LogIn(string _sMsg)
        {
            // _sMsg : {{$01234,req_user_log_in,id,pw$}}
            m_RPCom.recv_req_user_login(_id, _pw);

            // 판단

            // 회신
            string sResult, _Right, _Nak_Reason;
            m_RPCom.send_req_user_login_ack(sResult, _Right, _Nak_Reason)
        }

        // send work job
        private void button2_Click(object sender, EventArgs e)
        {
            CJobInfo job_info;
            job_info.sLotId = "lot-0001";
            job_info.sModel = "model-abc";
            job_info.nTotalProdCount = 1000;
            int nErr = m_RPCom.Send_Work_Job(job_info);
        }
    }
}
