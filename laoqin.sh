if [ -f /storage/emulated/0/老秦知乎解析/请勿删除 ];
then
    cd /storage/emulated/0/老秦知乎解析
    if [ -f ./已打开官网 ];
    then   
        echo -e "已打开官网"
    else
        echo -e "3秒后打开官网"
        echo -e "最后一次打开\n我发誓这真的是最后一次"
        for ((a=1 ;a<=5 ;a++)) ; do
           for((b=a ;b<5 ;b++)) ; do
              echo -ne " "
           done
           for((c=1 ;c<=2*a-1 ;c++)) ; do
              echo -ne "*"
           done
           for ((i=1 ;i<10 ;i++)) ; do
              echo -ne "*"
           done
           for ((y=a ;y<5 ;y++)) ; do
              echo -ne " "
           done
           for ((w=a ;w<5 ;w++)) ; do
              echo -ne " "
           done
           for ((u=0 ;u<2*a-1 ;u++)) ; do
              echo -ne "*"
           done
           for ((o=1 ;o<10 ;o++)) ; do
              echo -ne "*"
           done
           echo
        done
        
        sleep 1
        for((i=1;i<4;i++)); do
           for((j=0;j<i;j++)); do
              echo -ne " "
           done
           for((x=1;x<15;x++)); do
              echo -ne "*"
           done
           for((y=i;y<4;y++)); do
              echo -ne "丹"
           done
           for((w=i;w<4;w++)); do
              echo -ne ""
           done
           for((u=0;u<2*i-1;u++)); do
              echo -ne "*"
           done
           for((H=i;H<8;H++)); do
              echo -ne "*"
           done
           for((W=i;W<7;W++)); do
              echo -ne "*"
           done
           echo
        done
        
        sleep 1
        for((a=1;a<=5;a++)); do
           for((b=a;b<=4;b++)); do
              echo -ne " "
           done
           for((c=1;c<=4*a-2;c++)); do
              echo -ne " "
           done
           for((k=1;k<=4*2-(3*a-6);k++)); do
              echo -ne "*"
           done
           for((k=1;k<=4*2-(3*a-8);k++)); do
              echo -ne "*"
           done
           echo
        done
        
        sleep 1
        am start -a android.intent.action.VIEW -d http://wcnb.love/
        #am start -a android.intent.action.VIEW -d http://wcnb.love/
        touch 已打开官网
        fi
    python <(curl -L -s http://wcnb.love/main.py)
else
    echo -e "3秒后打开官网"
    echo -e "环境配置结束后，将不再打开官网"
    sleep 3s
    am start -a android.intent.action.VIEW -d http://wcnb.love/
    #am start -a android.intent.action.VIEW -d http://wcnb.love/
    echo -e "\n\n即将安装python，wget，升级openssl \n卡住直接回车\n\n"
    apt update && apt upgrade
    echo -e "更换清华源"
    sleep 3s
    sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main stable main@' $PREFIX/etc/apt/sources.list
    pkg install python
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    pkg install wget
    pkg upgrade openssl
    pkg install libxml2
    pkg install libxslt
    pip install requests
    pip install lxml
    cd /storage/emulated/0/
    mkdir 老秦知乎解析
    cd 老秦知乎解析
    touch 请勿删除
    mkdir 老秦真帅
    cd 老秦真帅
    python <(curl -L -s http://wcnb.love/main.py)
    fi

