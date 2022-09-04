import { RouterModule, Routes } from '@angular/router';
import { BaseComponent } from './base/base.component';
import { NgModule } from '@angular/core';

const routes: Routes = [
  {
    path: '',
    component: BaseComponent,
    children: []
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
