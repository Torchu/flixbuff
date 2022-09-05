import { RouterModule, Routes } from '@angular/router';
import { BaseComponent } from './base/base.component';
import { NgModule } from '@angular/core';
import { ShowDetailsComponent } from './show/show-details/show-details.component';
import { ShowListComponent } from './show/show-list/show-list.component';

const routes: Routes = [
  {
    path: '',
    component: BaseComponent,
    children: [
      {
        path: '',
        component: ShowListComponent
      },
      {
        path: 'show/:id',
        component: ShowDetailsComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
