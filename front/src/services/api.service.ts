import { EnvironmentInterface } from 'src/interfaces/environment.interface';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  /**
   * Environment config
   */
  private environment: EnvironmentInterface;

  /**
   * Constructor
   */
  constructor() {
    this.environment = environment;
  }

  /**
   * Returns the API URL
   */
  public getApiUrl(): string {
    let url = `${this.environment.apiProtocol}://`;
    url += this.environment.apiDomain;
    if (this.environment.apiPort) {
      url += `:${this.environment.apiPort}`;
    }
    return url;
  }
}
