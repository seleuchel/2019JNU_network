# #(1) send the ping message using UDP
# #(Note: Unlike TCP, you do not need to establish a connection first, since UDP is a connectionless protocol.)
# #(2) print the response message from server, if any
# #(3) calculate and print the round trip time (RTT), in seconds, of each packet, if server responses
# #(4) otherwise, print Request timed out
#
# from socket import *
# import time
#
# SERVERNAME = '127.0.0.1'
# SERVERPORT = 12000
#
# clientSocket = socket(AF_INET, SOCK_DGRAM)
# clientSocket.settimeout(1)
#
# rttList =[]
# allpingcnt = 0;
#
# wantoSend = 10;
#
# for i in range(wantoSend):
#     sendTime = time.time()
#     message = '[Ping] NUM : '+str(i+1)+'  timestamp : ' + str(time.strftime("%H:%M:%S"))
#     clientSocket.sendto(message,(SERVERNAME,SERVERPORT))
#
#     try:
#         pingMessage, serverAddress = clientSocket.recvfrom(1024)
#         recvTime = time.time()
#         rtt = recvTime - sendTime
#         print("Ping received >> ",pingMessage)
#         print("RTT >> ", rtt)
#         print("")
#
#         allpingcnt += 1
#         rttList.append(rtt*1000)
#
#     except timeout:
#         print("Request timed out")
#
# min = rttList[0]
# max = rttList[0]
#
# for j in range(len(rttList)):
#     if min > rttList[j]:
#         min = rttList[j]
#
#     if max < rttList[j]:
#         max = rttList[j]
#
# loss = float(wantoSend - allpingcnt)/wantoSend
#
# print("\n\nStatistics on " + str(SERVERNAME) + " : ")
# print("min :" + str(min) + "ms max :"  + str(max) + "ms avg :" + str(sum(rttList)/allpingcnt) +"ms\n")
# print("wantoSend :" + str(wantoSend) + ' Send : ' + str(allpingcnt))
# print("Packet Loss rate : {0}({1}%)\n".format(loss, loss*100))



from socket import *
import time

SERVERNAME = '127.0.0.1'
SERVERPORT = 8010

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)


for i in range(10):
    sendTime = time.time()
    message = 'Ping '+str(i+1)+' '+str(time.strftime("%H:%M:%S"))
    clientSocket.sendto(message,(SERVERNAME,SERVERPORT))

    try:
        pingMessage, serverAddress = clientSocket.recvfrom(1024)
        recvTime = time.time()
        rtt = recvTime - sendTime
        print("Ping received >> " + pingMessage)
        print("RTT >> " + str(rtt))
        print("")
        i += 1

    except timeout:
        print("Request timed out")
        print("")
