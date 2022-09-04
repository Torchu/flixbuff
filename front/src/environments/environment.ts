import { EnvironmentInterface } from 'src/interfaces/environment.interface';

/**
 * Development environment variables
 * @type {EnvironmentInterface}
 */
export const environment: EnvironmentInterface = {
  production: false,
  frontendDomain: 'localhost:4200',
  apiDomain: 'localhost',
  apiProtocol: 'http',
  apiPort: 5000
};
