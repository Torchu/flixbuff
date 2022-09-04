export interface EnvironmentInterface {
  production: boolean;
  frontendDomain: string;
  apiDomain: string;
  apiProtocol: 'http' | 'https';
  apiPort?: number;
}
