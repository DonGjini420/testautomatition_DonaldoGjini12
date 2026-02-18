import http from 'k6/http';
import { check } from 'k6';

export default function () {
  // Hämta lån från API:et
  const res = http.get(
    'https://kzmcpfklrqymzazaxlmv.supabase.co/functions/v1/partner-loan-api/loans',
    {
      headers: { 'x-api-key': '626125a0cad5d31395fdb24d7b6ba4e5080e14e75153491de96111e3c78d985e' }
    }
  );

  // Enkel check på status
  check(res, {
    'status is 200': r => r.status === 200
  });
}
