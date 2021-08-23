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
    req = AsapiRequest("slb", "2014-05-15", "DescribeLoadBalancers", api_gateway)

    #业务信息,具体可以参考对应的API说明
    req.add_query_param("Department", "3")


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
    as_client = ASClient("IDtLg7xElswktGPL", "p3YRKLqSlS5FSgvcu55rvsX3anO1Ch", "cn-jinan-sdhs-d01")
    response = as_client.do_request(req)

    print(response)


'''
slb DescribeLoadBalancers  版本2014-05-15
slb DescribeLoadBalancers  获取实例列表
slb   DescribeLoadBalancerAttribute  获取指定负载均衡实例的详细信息
'''