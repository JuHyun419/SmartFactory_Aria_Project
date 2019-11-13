using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SFClassWinForm
{
    /// <summary>
    /// 작업지시( MES Server -> Raspberry PI )
    /// Table Name - TBL_LOT
    /// </summary>
    public class CJobInfo
    {
        /// <summary>
        /// TBL_LOT 테이블의 컬럼
        /// </summary>
        public string sLotId;
        public string sModel;
        public int nTotalProdCount;
    }

    /// <summary>
    /// MES Server -> Raspberry PI 응답
    /// </summary>
    public class CRasberryPiCom
    {
        public int Send_Work_Job(CJobInfo _Job_Info)
        {
            return 0;
        }
    }

    /// <summary>
    /// MES Server <--> MES Client
    /// </summary>
    public class CMESClientCom
    {
        /// <summary>
        /// 로그인 확인 요청
        /// </summary>
        /// <param name="_id"></param>
        /// <param name="_pw"></param>
        /// <returns></returns>
        public int recv_req_user_login(string _id, string _pw)
        {
            return 0;
        }

        /// <summary>
        /// MES Client에서 보낸 로그인 확인 요청에 대한 응답
        /// </summary>
        /// <param name="_sResult">승인여부</param>
        /// <param name="_sRignt">권한</param>
        /// <param name="_nak_reason">거부 사유</param>
        /// <returns></returns>
        public int send_req_user_login_ack(string _sResult, string _sRignt, string _nak_reason)
        {
            return 0;
        }
    }

    public partial class fmMain : Form
    {
        /// <summary>
        /// PI, MES Client 객체 생성
        /// </summary>
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
