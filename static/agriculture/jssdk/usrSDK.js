/**
 * jssdk的初始化，具体的监听方法等
 * @chufucheng
 */

var USRSDK=function () {
    /**
     * 初始化jssdk
     */
    this.Jssdk_init={
        initJssdk:(name, token, dispatchServer)=>{
            window.jssdk.init(name, token, dispatchServer).then(() =>{
                console.log("===========websocket连接成功=============");
            }).catch(() =>{
                console.log("===========websocket连接失败=============");
            })
        }
    };


    /**
     *jssdk中具体的方法，监听，下发等
     */
    this._jssdk={
        //更新token
        setToken: (token)=>{
            window.jssdk.setToken(token);
        },
        //事件的监听，主要用于接收数据推送
        addListener: (name, param, fun)=>{
            window.jssdk.addListener(name, param, (deviceNoOrAccount,data) =>{
                let reviseData;
                switch(name){
                    //设备变量数据推送
                    case 'deviceData':
                        reviseData = {
                            'devId': deviceNoOrAccount,
                            'deviceId': deviceNoOrAccount,
                            'deviceName': data['deviceName'],
                            'dataPoints': data['dataPoints'],
                            'version': data['version']
                        };
                        break;
                    //设备上下线推送
                    case 'online':
                        reviseData = {
                            'account': deviceNoOrAccount,
                            'devId': data['deviceId'],
                            'devName': data['deviceName'],
                            'status': data['status'],
                            'time': data['time']
                        };
                        break;
                    //设备报警信息推送
                    case 'alarm':
                        data.dataPointName = data.dataPointName || data.datapointName;
                        data.pointId = data.pointId || data.dataPointId;
                        reviseData = {
                            'account': deviceNoOrAccount,
                            'devId': data['deviceId'],
                            'slaveIndex':data['slaveIndex'],
                            'slaveAddr':data['slaveAddr'],
                            'alarmState': data,
                            'time': data['time']
                        };
                        break;
                }
                fun(reviseData)
            })
        },
        //移除监听器
        removeEventListener: (name, param)=>{
            window.jssdk.removeEventListener(name, param)
        },
        //向设备变量发送数据
        setDataPoint: (deviceNo, datapoints)=>{
            window.jssdk.setDataPoint(deviceNo, datapoints);
        },
        //查询设备变量数据
        queryDataPoint: (deviceNo, datapoints)=>{
            window.jssdk.queryDataPoint(deviceNo, datapoints);
        },
        //获取设备变量最后一条数据
        getLastDataHistory: (datapoints, fun)=>{
            window.jssdk.getLastDataHistory({"devDatapoints": datapoints}).then(function(data){
                fun(data)
            },function(err){
                console.log('err',err);
            });
        },
        //获取历史记录
        getDataHistory: (param, fun)=>{
            window.jssdk.getDataHistory(param).then(function(data){
                fun(data)
            },function(err){
                console.log('err',err);
            });
        },

    }

};