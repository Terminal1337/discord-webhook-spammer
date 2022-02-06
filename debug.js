//Debug Spammer
const https = require('http');

const options = {};
var j = {
    tt:0,
    rps:0
};
class DB {
    static get json() {
        return (typeof j == "object") ? j : {}
    }
    static set json(v) {
        return (typeof v == "object") ? object : j;
    }
    static get tt() {
        return j['tt'];
    }
    static set tt(v) {
        j['tt'] = v
    }
    static get rps() {
        return j['rps']
    }
    static set rps(v) {
        j['rps'] = v
    }
}

setInterval(function() {
    DB.rps = 0
},1000)

function uptoLastTwoDecimals(num) {
    return (Math.round(num * 100) / 100).toFixed(2);
}
function updateHeaders(tries , rps) {
    process.title = `Webhook Spammer Debug [Total Requests: ${tries} | RPS: ${rps}]`
}
function handleHeaders(tt , rps) {
    DB.tt += tt;
    DB.rps += rps
    updateHeaders(DB.tt , DB.rps);
}
handleHeaders(0,0)

https.createServer(options, (req, res) => {
  const ip = res.socket.remoteAddress;
  const port = res.socket.remotePort;
  if (req.method.toLowerCase() == 'post') {
    console.log(`[+] Got a Message Send Request by ${ip}`);
    handleHeaders(1,1)
    res.writeHead(204);
    res.end(`{"this":"made by https://github.com/titan3301 >_<"}`);
  } else {
    console.log(`[+] Got a Fetch Request by ${ip}`)
    res.writeHead(200);
    res.end(`{"this":"made by https://github.com/titan3301 >_<"}`);
  }
}).listen(8001 , () => {
    console.log(`[+] Listening at port 8001 addr http://127.0.0.1:8001/\n`)
});