import sys
import numpy as np
from PIL import Image
import io
import flags
from mmocr.utils.ocr import MMOCR
import json

if not hasattr(sys, 'argv'):
    sys.argv = ['']


'''
服务初始化
@param config:
    插件初始化需要的一些配置，字典类型
    key: 配置名
    value: 配置的值
@return
    ret: 错误码。无错误时返回0
'''


model = None

logger = flags.logger

def wrapperInit(config: dict) -> int:
    logger.info("model initializing...")
    logger.info("engine config %s" % str(config))
    global model
    # Load models into memory
    model = MMOCR(det='TextSnake', recog=None)
    logger.info("init success")
    return 0



'''
服务逆初始化
@return
    ret:错误码。无错误码时返回0
'''


def wrapperFini() -> int:
    return 0


'''
非会话模式计算接口,对应oneShot请求,可能存在并发调用
@param usrTag 句柄
#param params 功能参数
@param  reqData     写入数据实体
@param  respData    返回结果实体,内存由底层服务层申请维护,通过execFree()接口释放
@param psrIds 需要使用的个性化资源标识列表
@param psrCnt 需要使用的个性化资源个数
@return 接口错误码
    reqDat
    ret:错误码。无错误码时返回0
'''


def wrapperOnceExec(usrTag: str, params: dict, reqData: list, respData: list, psrIds: list, psrCnt: int) -> int:
    img = np.array(Image.open(io.BytesIO(reqData[0]["data"])).convert('RGB'))
    global model
    rlt = model.readtext(img,details=True)
    rlt = json.dumps(rlt)
    respData.append({"key": "boxes", "data": rlt, "len": len(rlt), "status": 3, "type": 0})
    #respData.append(rlt)
    print(respData, flush=True)
    return 0



def wrapperCreate(usrTag: str, params: list, psrIds: list, psrCnt: int) -> str:
    return ""


def wrapperWrite(handle: str, datas: list) -> int:
    return 0


def wrapperRead(handle: str) -> list:
    return list


def wrapperDestroy(handle: str) -> int:
    return 0


def wrapperError(ret: int) -> str:
    if ret == 10013:
        return "reqData is empty"
    elif ret == 10001:
        return "load onnx model failed"
    else:
        return "other error code"
