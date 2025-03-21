# run again.  Do not edit this file unless you know what you are doing.
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QMetaObject, QRect, QSize, Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy, QHBoxLayout, QVBoxLayout, \
    QCheckBox

from videotrans.configure import config
from videotrans.util import tools


class Ui_gptsovitsform(object):
    def setupUi(self, gptsovitsform):
        self.has_done = False
        if not gptsovitsform.objectName():
            gptsovitsform.setObjectName("gptsovitsform")
        gptsovitsform.setWindowModality(Qt.NonModal)
        gptsovitsform.resize(600, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(gptsovitsform.sizePolicy().hasHeightForWidth())
        gptsovitsform.setSizePolicy(sizePolicy)
        gptsovitsform.setMaximumSize(QSize(600, 500))

        self.wrap_h = QHBoxLayout(gptsovitsform)
        self.wrap_h.setObjectName(u"wrap_h")
        self.inner_v= QVBoxLayout()

        h1= QHBoxLayout()
        self.label = QLabel()
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(0, 35))
        self.api_url = QLineEdit()
        self.api_url.setObjectName("api_url")
        self.api_url.setMinimumSize(QSize(0, 35))
        h1.addWidget(self.label)
        h1.addWidget(self.api_url)
        self.inner_v.addLayout(h1)

        h2= QHBoxLayout()
        self.label_3 = QLabel()
        self.label_3.setObjectName("label_3")

        self.extra = QLineEdit()
        self.extra.setObjectName("extra")
        self.extra.setMinimumSize(QSize(0, 35))
        h2.addWidget(self.label_3)
        h2.addWidget(self.extra)
        self.inner_v.addLayout(h2)

        self.label_4 = QLabel()
        self.label_4.setObjectName("label_4")
        self.label_4.setMinimumSize(QSize(301, 16))
        self.label_4.setText('参考音频#音频文字内容#语言代码')

        self.role = QPlainTextEdit()
        self.role.setObjectName("role")
        self.role.setMinimumSize(QSize(571, 100))
        self.role.setReadOnly(False)
        self.inner_v.addWidget(self.label_4)
        self.inner_v.addWidget(self.role)

        self.label_5 = QLabel()
        self.label_5.setObjectName("label_5")
        self.label_5.setMinimumSize(QSize( 301, 16))
        self.label_5.setText('API请求说明')
        self.inner_v.addWidget(self.label_5)

        self.tips = QPlainTextEdit()
        self.tips.setObjectName("tips")
        self.tips.setMinimumSize(QSize(571, 150))
        self.tips.setReadOnly(True)
        self.inner_v.addWidget(self.tips)


        h3=QHBoxLayout()
        self.is_v2=QCheckBox()
        self.is_v2.setText("api_v2?")
        self.is_v2.setToolTip("如果是api_v2.py,则必须选中")
        self.save = QPushButton()
        self.save.setObjectName("save")
        self.save.setMinimumSize(QSize(0, 35))
        h3.addWidget(self.is_v2)
        h3.addWidget(self.save)
        self.test = QPushButton()
        self.test.setObjectName("test")
        self.test.setMinimumSize(QSize(0, 35))
        help_btn = QtWidgets.QPushButton()
        help_btn.setMinimumSize(QtCore.QSize(0, 35))
        help_btn.setStyleSheet("background-color: rgba(255, 255, 255,0)")
        help_btn.setObjectName("help_btn")
        help_btn.setCursor(Qt.PointingHandCursor)
        help_btn.setText("查看填写教程" if config.defaulelang == 'zh' else "Fill out the tutorial")
        help_btn.clicked.connect(lambda: tools.open_url(url='https://pyvideotrans.com/gptsovits'))

        h3.addWidget(self.test)
        h3.addWidget(help_btn)
        self.inner_v.addLayout(h3)


        # end
        self.wrap_h.addLayout(self.inner_v)

        self.retranslateUi(gptsovitsform)

        QMetaObject.connectSlotsByName(gptsovitsform)

    # setupUi

    def retranslateUi(self, gptsovitsform):
        tips = """
将以POST请求向填写的API地址发送application/json数据：

GPT-SoVITS自带api.py，可接受请求共包含5个参数

text,text_language,refer_wav_path,prompt_text,prompt_language

因该api.py不可动态切换模型，因此后3个参数可在启动api.py时指定，在此请求时不发送
GPT-SoVITS启动时指定命令`python api.py -dr "参考音频路径"  -dt "参考音频文本" -dl "参考音频语言代码" `

本工具将向填写的API地址发送以下4个参数，后2个为冗余暂未使用

text:需要合成的文本/字符串
text_language:文字所属语言代码(zh|ja|en)/字符串


ostype:win32或mac或linux操作系统类型/字符串
extra:额外参数/字符串

请求失败时返回：
{
    "code": 400, 错误数
    "message": "错误信息"
}            
请求成功时返回音频流
"""

        gptsovitsform.setWindowTitle("GPT-SoVITS API")
        self.label_3.setText("额外参数")
        self.role.setPlaceholderText("在此填写参考音频信息,可以不填写，格式如下\n例如：一行一组\n123.wav#你好啊我的朋友#zh")
        self.tips.setPlainText(tips)
        self.save.setText("保存" if config.defaulelang == 'zh' else "Save")
        self.api_url.setPlaceholderText("填写http开头的完整地址,GPT-SoVITS自带api默认 http://127.0.0.1:9880")
        self.label.setText("GPT-SoVITS API")
        self.extra.setPlaceholderText("填写通过extra键向api传递的额外参数，为空则传递pyvideotrans")
        self.test.setText("测试Api" if config.defaulelang == 'zh' else "Test API")
    # retranslateUi
