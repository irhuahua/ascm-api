
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
    req = AsapiRequest("OneRouter", "2018-12-12", "DoOpenApi", api_gateway)

    #业务信息,具体可以参考对应的API说明
    req.add_query_param("Action", "DoOpenApi")
    req.add_query_param("Product", "OneRouter")
    req.add_query_param("Version", "2018-12-12")
    req.add_query_param("RegionId", "cn-jinan-sdhs-d01")
    req.add_query_param("ProductName", "oss")
    req.add_query_param("OpenApiAction", "GetBucketStorageCapacity")
    req.add_query_param("params",'{"BucketName":"user-image","region":"cn-jinan-sdhs-d01"}')
    req.add_query_param("Department", "3")
    req.add_query_param("AccountInfo", "aaa")

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
as_client = ASClient("0bnnnwbHEcpWRl2k", "BAmirM01cB3unSl3Tz8ZRVpf2iqgA7", "cn-jinan-sdhs-d01")


[root@r010c4001.cloud.c4.am1 /root] 山东高速OPS1 
#curl "http://server.asapi.cn-jinan-sdhs-d01.ops.sdhs.cloud/asapi/v3?Action=DoOpenApi&Product=OneRouter&Version=2018-12-12&AccessKeyId=0bnnnwbHEcpWRl2k&AccessKeySecret=BAmirM01cB3unSl3Tz8ZRVpf2iqgA7&RegionId=cn-jinan-sdhs-d01&ProductName=oss&OpenApiAction=GetBucketStorageCapacity&AccountInfo=aaa&Department=3&Params=\{\"BucketName\":\"bucket-jtzh\",\"region\":\"cn-jinan-sdhs-d01\"\}"
{"Data":{"BucketUserQos":{"StorageCapacity":"5000"}},"RequestId":"611CB84C458DCFB3BD52AE2B"}
[root@r010c4001.cloud.c4.am1 /root] 山东高速OPS1 
#
oneconsole签名使用的，使用用户ak调用时，传递一个“”空字符串就行，后端会根据参数处理的
'''