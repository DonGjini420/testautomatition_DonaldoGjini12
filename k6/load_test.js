import http from 'k6/http';
import { check, sleep } from 'k6';

const API_KEY = '626125a0cad5d31395fdb24d7b6ba4e5080e14e75153491de96111e3c78d985e';
const BASE_URL = 'https://kzmcpfklrqymzazaxlmv.supabase.co/functions/v1/partner-loan-api';

const testData = [
  {
    applicantName: 'Test Andersson',
    applicantEmail: 'test1@example.com',
    applicantPhone: '+46701234567',
    personalNumber: '199503152679',
    loanAmount: 50000,
    loanType: 'car',
    loanTerm: 24,
    monthlyIncome: 30000,
    existingDebts: 10000,
    employmentStatus: 'employed',
    address: 'Storgatan 1, 123 45 Stockholm, Sweden',
  },
  {
    applicantName: 'Stora Belopp Svensson',
    applicantEmail: 'test2@example.com',
    applicantPhone: '+46702345678',
    personalNumber: '199105053217',
    loanAmount: 300000,
    loanType: 'renovation',
    loanTerm: 60,
    monthlyIncome: 75000,
    existingDebts: 50000,
    employmentStatus: 'employed',
    address: 'Villagatan 10, 456 78 Göteborg, Sweden',
  },
  {
    applicantName: 'Bröllops Person',
    applicantEmail: 'test3@example.com',
    applicantPhone: '+46703456789',
    personalNumber: '199510072710',
    loanAmount: 100000,
    loanType: 'wedding',
    loanTerm: 36,
    monthlyIncome: 45000,
    existingDebts: 0,
    employmentStatus: 'employed',
    address: 'Kyrkkvägen 5, 789 01 Västerås, Sweden',
  },
  {
    applicantName: 'Semester Andersson',
    applicantEmail: 'test4@example.com',
    applicantPhone: '+46704567890',
    personalNumber: '199212345678',
    loanAmount: 30000,
    loanType: 'vacation',
    loanTerm: 12,
    monthlyIncome: 35000,
    existingDebts: 5000,
    employmentStatus: 'employed',
    address: 'Semestergatan 12, 234 56 Malmö, Sweden',
  },
];

export const options = {
  stages: [
    { duration: '30s', target: 5 },
    { duration: '1m30s', target: 5 },
    { duration: '30s', target: 0 },
  ],
  thresholds: {
    'http_req_duration': ['p(95)<500', 'p(99)<1000'],
    'http_req_failed': ['rate<0.1'],
  },
};

export default function () {
  const app = testData[Math.floor(Math.random() * testData.length)];

  const res = http.post(`${BASE_URL}/loans`, JSON.stringify(app), {
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': API_KEY,
    },
  });

  check(res, {
    'status is 201': (r) => r.status === 201,
    'has loan id': (r) => r.json('id') || r.json('loanId'),
    'applicant name matches': (r) => r.json('applicantName') === app.applicantName,
    'loan amount matches': (r) => r.json('loanAmount') === app.loanAmount,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });

  sleep(1);
}
