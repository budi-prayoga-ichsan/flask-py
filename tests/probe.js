
import http from 'k6/http';
import { sleep, check } from 'k6';
import { Trend } from 'k6/metrics';

const probeResponseTime = new Trend('probe_response_time');

export const options = {
    vus: 1,
    duration: '30s',
};

export default function () {
    const res = http.get('http://127.0.0.1:5000/search?q=Andi');

    check(res, {
        'probe status is 200': (r) => r.status === 200,
    });

    if (res.status > 0) {
        probeResponseTime.add(res.timings.duration);
    }

    sleep(2);
}
