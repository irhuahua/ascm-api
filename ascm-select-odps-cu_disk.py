from aliyunsdkasapi.ASClient import ASClient
from aliyunsdkasapi.AsapiRequest import AsapiRequest

if __name__ == '__main__':

    #接口信息
    api_gateway = "http://server.asapi.cn-jinan-sdhs-d01.ops.sdhs.cloud/asapi/v3" # 参考《获取ASAPI的endpoint》
    '''
    	创建AsapiRquest参数说明：
        	参数1: 对应公共参数Product(API产品名称)
            参数2: 对应公共参数Version(API版本)
            参数3: 对应公共参数Action(API名称)
            参数4: 对应ASAPI的服务endpoint
    '''
    req = AsapiRequest("ascm", "2019-05-10", "ListOdpsEngineQuota", api_gateway)

    #业务信息,具体可以参考对应的API说明
    req.add_query_param("id", "26")


    #Header信息


    #请求类型，默认GET,可以省略
    req.set_method("GET")

    #用环境信息初始化ASClient，参考《获取AccessKey》
    '''
    	ASClient初始化参数说明：
        	参数1: 对应公共参数AccessKeyId
            参数2: 对应公共参数AccessKeySecret
            参数3：对应公共参数RegionId
    '''
    as_client = ASClient("0bnnnwbHEcpWRl2k", "BAmirM01cB3unSl3Tz8ZRVpf2iqgA7", "cn-jinan-sdhs-d01")
    response = as_client.do_request(req)

    print(response)


'''
这个id为上一个api获取的engineId
这里的disk 为1 表示1*1024G
'''