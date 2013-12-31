create table fanfou(
id int(6) primary key auto_increment ,  #message id
source int(1) not null,                 #来源 xml=0  私信=1  微信文字=2  微信图片=3
over bool default 0,                    #是否发送 未发送=0  发送=1
content varchar(250)                    #message   长度为250字
)CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
