namespace XmlWriteTest
{
    partial class Form1
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent()
        {
            this.btn_XmlWrite = new System.Windows.Forms.Button();
            this.btn_XmlRead = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.label_SystemByte = new System.Windows.Forms.Label();
            this.label_CMD = new System.Windows.Forms.Label();
            this.label_Stream = new System.Windows.Forms.Label();
            this.label_Function = new System.Windows.Forms.Label();
            this.label_HCACK = new System.Windows.Forms.Label();
            this.txt_SystemByte = new System.Windows.Forms.TextBox();
            this.txt_CMD = new System.Windows.Forms.TextBox();
            this.txt_Stream = new System.Windows.Forms.TextBox();
            this.txt_Function = new System.Windows.Forms.TextBox();
            this.txt_HCACK = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // btn_XmlWrite
            // 
            this.btn_XmlWrite.Location = new System.Drawing.Point(12, 415);
            this.btn_XmlWrite.Name = "btn_XmlWrite";
            this.btn_XmlWrite.Size = new System.Drawing.Size(75, 23);
            this.btn_XmlWrite.TabIndex = 0;
            this.btn_XmlWrite.Text = "XmlWrite";
            this.btn_XmlWrite.UseVisualStyleBackColor = true;
            this.btn_XmlWrite.Click += new System.EventHandler(this.Btn_XmlWrite_Click);
            // 
            // btn_XmlRead
            // 
            this.btn_XmlRead.Location = new System.Drawing.Point(218, 415);
            this.btn_XmlRead.Name = "btn_XmlRead";
            this.btn_XmlRead.Size = new System.Drawing.Size(75, 23);
            this.btn_XmlRead.TabIndex = 1;
            this.btn_XmlRead.Text = "XmlRead";
            this.btn_XmlRead.UseVisualStyleBackColor = true;
            this.btn_XmlRead.Click += new System.EventHandler(this.Btn_XmlRead_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(299, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(489, 426);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // label_SystemByte
            // 
            this.label_SystemByte.AutoSize = true;
            this.label_SystemByte.Location = new System.Drawing.Point(10, 15);
            this.label_SystemByte.Name = "label_SystemByte";
            this.label_SystemByte.Size = new System.Drawing.Size(73, 12);
            this.label_SystemByte.TabIndex = 3;
            this.label_SystemByte.Text = "SystemByte";
            // 
            // label_CMD
            // 
            this.label_CMD.AutoSize = true;
            this.label_CMD.Location = new System.Drawing.Point(10, 45);
            this.label_CMD.Name = "label_CMD";
            this.label_CMD.Size = new System.Drawing.Size(33, 12);
            this.label_CMD.TabIndex = 4;
            this.label_CMD.Text = "CMD";
            // 
            // label_Stream
            // 
            this.label_Stream.AutoSize = true;
            this.label_Stream.Location = new System.Drawing.Point(10, 71);
            this.label_Stream.Name = "label_Stream";
            this.label_Stream.Size = new System.Drawing.Size(45, 12);
            this.label_Stream.TabIndex = 5;
            this.label_Stream.Text = "Stream";
            // 
            // label_Function
            // 
            this.label_Function.AutoSize = true;
            this.label_Function.Location = new System.Drawing.Point(10, 101);
            this.label_Function.Name = "label_Function";
            this.label_Function.Size = new System.Drawing.Size(53, 12);
            this.label_Function.TabIndex = 6;
            this.label_Function.Text = "Function";
            // 
            // label_HCACK
            // 
            this.label_HCACK.AutoSize = true;
            this.label_HCACK.Location = new System.Drawing.Point(12, 228);
            this.label_HCACK.Name = "label_HCACK";
            this.label_HCACK.Size = new System.Drawing.Size(47, 12);
            this.label_HCACK.TabIndex = 7;
            this.label_HCACK.Text = "HCACK";
            // 
            // txt_SystemByte
            // 
            this.txt_SystemByte.Location = new System.Drawing.Point(96, 6);
            this.txt_SystemByte.Name = "txt_SystemByte";
            this.txt_SystemByte.Size = new System.Drawing.Size(100, 21);
            this.txt_SystemByte.TabIndex = 8;
            // 
            // txt_CMD
            // 
            this.txt_CMD.Location = new System.Drawing.Point(96, 36);
            this.txt_CMD.Name = "txt_CMD";
            this.txt_CMD.Size = new System.Drawing.Size(100, 21);
            this.txt_CMD.TabIndex = 9;
            // 
            // txt_Stream
            // 
            this.txt_Stream.Location = new System.Drawing.Point(96, 68);
            this.txt_Stream.Name = "txt_Stream";
            this.txt_Stream.Size = new System.Drawing.Size(100, 21);
            this.txt_Stream.TabIndex = 10;
            // 
            // txt_Function
            // 
            this.txt_Function.Location = new System.Drawing.Point(96, 97);
            this.txt_Function.Name = "txt_Function";
            this.txt_Function.Size = new System.Drawing.Size(100, 21);
            this.txt_Function.TabIndex = 11;
            // 
            // txt_HCACK
            // 
            this.txt_HCACK.Location = new System.Drawing.Point(96, 221);
            this.txt_HCACK.Name = "txt_HCACK";
            this.txt_HCACK.Size = new System.Drawing.Size(100, 21);
            this.txt_HCACK.TabIndex = 12;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.txt_HCACK);
            this.Controls.Add(this.txt_Function);
            this.Controls.Add(this.txt_Stream);
            this.Controls.Add(this.txt_CMD);
            this.Controls.Add(this.txt_SystemByte);
            this.Controls.Add(this.label_HCACK);
            this.Controls.Add(this.label_Function);
            this.Controls.Add(this.label_Stream);
            this.Controls.Add(this.label_CMD);
            this.Controls.Add(this.label_SystemByte);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.btn_XmlRead);
            this.Controls.Add(this.btn_XmlWrite);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btn_XmlWrite;
        private System.Windows.Forms.Button btn_XmlRead;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Label label_SystemByte;
        private System.Windows.Forms.Label label_CMD;
        private System.Windows.Forms.Label label_Stream;
        private System.Windows.Forms.Label label_Function;
        private System.Windows.Forms.Label label_HCACK;
        private System.Windows.Forms.TextBox txt_SystemByte;
        private System.Windows.Forms.TextBox txt_CMD;
        private System.Windows.Forms.TextBox txt_Stream;
        private System.Windows.Forms.TextBox txt_Function;
        private System.Windows.Forms.TextBox txt_HCACK;
    }
}

