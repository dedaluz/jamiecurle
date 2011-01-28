class JournalsController < ApplicationController
  # GET /journals
  # GET /journals.xml
  
  def index
    @journals = Journal.all(:order => 'created_at DESC')
  end

  # GET /journals/1
  # GET /journals/1.xml
  def show
    @journal = Journal.find(params[:id])
  end

  def new
    @journal = Journal.new
  end

  def edit
    @journal = Journal.find(params[:id])
  end

  def create
    @journal = Journal.new(params[:journal])

      if @journal.save
        redirect_to(@journal, :notice => 'Journal was successfully created.')
      else
        render :action => "new"
      end
  end

  def update
    @journal = Journal.find(params[:id])


      if @journal.update_attributes(params[:journal])
        redirect_to(edit_journal_path, :notice => 'Journal was successfully updated.')
      else
        render :action => "edit"
      end
  end

  def destroy
    @journal = Journal.find(params[:id])
    @journal.destroy
  end
end
