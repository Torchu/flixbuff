import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MatDialog } from '@angular/material/dialog';
import { ReviewCreateComponent } from 'src/app/review/review-create/review-create.component';
import { Show } from 'src/models/show';
import { ShowService } from 'src/services/show.service';

@Component({
  selector: 'app-show-details',
  templateUrl: './show-details.component.html',
  styleUrls: ['./show-details.component.scss']
})
export class ShowDetailsComponent implements OnInit {
  show: Show;

  constructor(private showService: ShowService, private route: ActivatedRoute, private dialog: MatDialog) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.showService.get(params['id']).subscribe((show: Show) => {
        this.show = show;
      });
    });
  }

  /**
   * Open a dialog to create a review
   */
  openReviewDialog(seasonIndex: number): void {
    this.dialog.open(ReviewCreateComponent, {
      width: '500px',
      height: '50%',
      panelClass: 'custom-dialog',
      data: { show: this.show, season: this.show.seasons[seasonIndex] }
    });
  }
}
