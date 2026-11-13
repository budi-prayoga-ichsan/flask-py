
import http from 'k6/http';
import { sleep, check } from 'k6';
import { Trend } from 'k6/metrics';

const responseTime = new Trend('response_time_custom');

export const options = {
    vus: 200,
    duration: '30s',
};

export default function () {
    const res = http.get('http://127.0.0.1:5000/search?q=Andi');

    check(res, {
        'status is 200': (r) => r.status === 200,
    });

    if (res.status > 0) {
        responseTime.add(res.timings.duration);
    }

    sleep(1);
}
